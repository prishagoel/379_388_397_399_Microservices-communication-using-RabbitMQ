from producer1 import OrdersProducer  

producer = OrdersProducer()

producer.send_message("insert")

producer.close_connection()

from consumer1 import OrdersConsumer  

consumer = OrdersConsumer()

consumer.start_consuming()
