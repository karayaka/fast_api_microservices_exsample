import asyncio

# env Variable
KAFKA_BOOTSTRAP_SERVERS= "localhost:9093"
KAFKA_TOPIC="commets"
KAFKA_CONSUMER_GROUP="comments_count"
loop = asyncio.get_event_loop()