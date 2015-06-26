first on terminal:
> mongod --dbpath ./backend/xernbase/data --logpath ./xernbase/log/xern.log --journal
*** this sets the dbpath and logpath and opens a local connection in the xern folder ***
*** NOTE: the last --journal is only necessary on 32-bit win processors to the best of my knowledge ***

second terminal window:
> mongo
'' not necessary but it just checks that mongod ran properly
> show dbs
'' this will show you preetham exists
> use preetham
''  this will switch to preetham db
> db.getCollectionNames()
''  this will return ["sidhanth", "system.indexes"]

third terminal window:
python
>> from pymongo import *
>> client = MongoClient()
>> client.database_names()
['local', 'preetham']
>> db = client.preetham
>> db.collection_names()
['sidhanth', 'system.indexes']
>> coll = db.sidhanth
>> for each in coll.find():
... print (each)
# should print dict
