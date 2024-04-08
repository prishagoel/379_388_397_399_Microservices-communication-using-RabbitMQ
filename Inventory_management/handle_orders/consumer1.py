import pika
#from .models import Inventory

class OrdersConsumer:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='orders_queue')
        self.channel.basic_consume(queue='orders_queue', on_message_callback=self.callback, auto_ack=True)
        print("Consumer1 initialized.")

    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body)
        print("Message received:", body)
        
        if body == b'peek':
            self.peek_orders()
        elif body == b'insert':
            self.insert_orders()
        else:
            print("Invalid message received, ignored:", body)

    def peek_orders(self):
        print("Peek message received. Viewing orders...")
        '''items = Inventory.objects.all()
        for item in items:
            print(f"{item.item}: {item.quantity}")'''

    def insert_orders(self):
        print("Insert message received. Inserting order for a particular product...")

    def start_consuming(self):
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def close_connection(self):
        self.connection.close()
        print("Connection closed.")
