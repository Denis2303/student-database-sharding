from pymongo import MongoClient
import time

client = MongoClient('mongodb://localhost:27017/')

time.sleep(10)

client.admin.command('addShard', 'shard1ReplSet/shard1-1:27017,shard1-2:27017')
client.admin.command('addShard', 'shard2ReplSet/shard2-1:27017,shard2-2:27017')
client.admin.command('addShard', 'shard3ReplSet/shard3-1:27017,shard3-2:27017')

client.admin.command('enableSharding', 'universityDB')

db = client.universityDB
db.students.create_index('student_id')
client.admin.command('shardCollection', 'universityDB.students', key={'student_id': 'hashed'})
print('111111111111111111111111')
time.sleep(10)