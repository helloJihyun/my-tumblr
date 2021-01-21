from pymongo import MongoClient

mongodb_id = 'jihyun'
mongodb_pwd = 'jihyun9802'
public_ip_address = '54.180.108.228'

local_client = MongoClient('localhost', 27017)
aws_client = MongoClient('mongodb://%s:%s@%s'%(mongodb_id, mongodb_pwd, public_ip_address), 27017)

db_name = 'my_tumblr'

db_local = local_client.get_database(db_name)
db_aws = aws_client.get_database(db_name)

for collection in db_local.list_collection_names():
    for record in db_local.get_collection(collection).find():
        db_aws.get_collection(collection).insert_one(record)
