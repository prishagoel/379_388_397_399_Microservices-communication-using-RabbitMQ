from producer import InventoryProducer 

producer = InventoryProducer()

producer.send_message("insert")

producer.close_connection()

from consumer import InventoryConsumer  

consumer = InventoryConsumer()

consumer.start_consuming()
