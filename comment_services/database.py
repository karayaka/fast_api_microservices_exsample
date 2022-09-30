from pymongo import MongoClient

cliend= MongoClient(host='localhost', port=27017, document_class=dict, tz_aware=False, connect=True,)

db=cliend['fastapi_blog_comments']

comments=db.comments
