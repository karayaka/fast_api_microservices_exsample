from pydoc_data.topics import topics
from tokenize import group
from schema import CommentCountMessage as ccm
from aiokafka import AIOKafkaProducer
import json
from message_broker_config import KAFKA_BOOTSTRAP_SERVERS,KAFKA_TOPIC,loop

 
async def comment_count_message(message:ccm):
    producer=AIOKafkaProducer(loop=loop,bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    try:
        value_json=json.dumps(message.__dict__).encode('utf-8')
        await producer.send_and_wait(topic=KAFKA_TOPIC,value=value_json)
    finally:
        await producer.stop()