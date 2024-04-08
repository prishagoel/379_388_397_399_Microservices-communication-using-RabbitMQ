import pika
#from .models import Inventory

class InventoryConsumer:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='inventory_queue')
        self.channel.basic_consume(queue='inventory_queue', on_message_callback=self.callback, auto_ack=True)
        print("Consumer initialized.")

    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body)
        print("Message received:", body)
        
        if body == b'peek':
            self.peek_inventory()
        elif body == b'insert':
            self.insert_inventory()
        elif body in [b'laptop', b'monitors', b'keyboard', b'tablet', b'printer']:
            self.refill_stock(body.decode())  #Decode bytes to string
        else:
            print("Invalid message received, ignored:", body)

    def peek_inventory(self):
        print("Peek message received. Viewing product names and quantities...")
        '''items = Inventory.objects.all()
        for item in items:
            print(f"{item.item}: {item.quantity}")'''

    def insert_inventory(self):
        print("Insert message received. Inserting stock for a particular product...")

    def refill_stock(self, product_name):
        print(f"Refill stock message received for product: {product_name}")

    def start_consuming(self):
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def close_connection(self):
        self.connection.close()
        print("Connection closed.")
