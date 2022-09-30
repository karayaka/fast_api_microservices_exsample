from pymongo import MongoClient

cliend= MongoClient(host='localhost', port=27017, document_class=dict, tz_aware=False, connect=True,)

db=cliend['fastApiAuthServices']

users=db.users
