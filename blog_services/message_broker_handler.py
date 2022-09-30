from schema import CommentCountMessage as ccm
from aiokafka import AIOKafkaConsumer
import json
from message_broker_config import KAFKA_BOOTSTRAP_SERVERS,KAFKA_CONSUMER_GROUP,KAFKA_TOPIC,loop

 # arka pla nserviisnde 
async def commet_count_consume():
    consumer=AIOKafkaConsumer(KAFKA_TOPIC,loop=loop,bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,group_id=KAFKA_CONSUMER_GROUP)
    await consumer.start()
    try:
        async for msg in consumer:
            print(msg)
    finally:
        await consumer.stop()