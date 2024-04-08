import pika

class OrdersProducer:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='orders_queue')
        print("Producer1 initialized.")

    def send_message(self, message):
        self.channel.basic_publish(exchange='', routing_key='orders_queue', body=message)
        print("[x] Sent %r" % message)
        print("Message sent.")

    def close_connection(self):
        self.connection.close()
        print("Connection closed.")
