from pymongo import *
from base_class import *
from helperfile import *

connection = MongoClient() 
'''
edit this by giving MongoClient()
an appropriate argument for the database address on the server
'''


''' creates a collection named 'xernbase' and assigns the variable
xern_database to the created database '''
xernbase = connection.get_database('xernbase')

''' creates a collection named 'userCollection' and assigns the variable
user_collection to the created collection '''
user_collection = xernbase.userCollection

''' creates a collection named 'tags' and assigns the variable tag_Collection
to the created collection '''
tag_collection = xernbase.tagCollection

class globalAction:    
    ''' this class defines actions that can
       be performed on the user database '''
    
    def __init__(self):
        self.usercount = 0

    ''' adds a user to the database when he/she creates a
       new account '''
    def addUser(self, userDict):
        self.usercount += 1
        user_collection.insert_one(userDict)
    
    ''' updates arbitrary user information
       updateDict is a dictionary of the form
       {'$set' : {'Michael Liang' : 'Chimchar'}} 
       That set will be obtained from user input by
       a function like synthesizeUpdateDict in frontend '''
    def updateUser(self, userID, updateDict):
        user_collection.update({"user" : userID}, updateDict)

    ''' increaseTagWeight : user * tag * int
        requires : userID is a valid user. Tag already exists in global
        tag
        ensures : updates the weight of the desired tag and updates
                  the total sum of weights'''    
    def increaseTagWeight (self, userID, tagName, tagIncrement) {
        tagDict = retrieve(['tags'], user_collection, {"user" : userID})
        if (tagName not in tagDict):
            tagDict[tagName] = tagIncrement
        else:
            tagDict[tagName] += tagIncrement
        self.updateUser(userID, {'$set' : {'tags' : tagDict}}
        tagTotal = retrieve(['tagtotal'], user_collection, {'user'\
                    : userID}) + tagIncrement
        self.updateUser(userID, {'$set' : {'tagtotal' : tagTotal}})


    '''
    updateTag : string -> void
    Requires : Nothing
    Ensures : updates the globalTag so that newTag
              is stored as a user accessible tag
    '''
    def updateTag(self, newTag):
        newTag = stringJoin(newTag.split(" "))
        if (not (newTag in mongohelper.retrieve(["tagset"], tag_collection))):
            tagList = mongohelper.retrieve(["taglist"], tag_collection).\
            append(newTag)
            tag_collection.update({"tag" : "tagid"},\
            {"$set" : {"taglist" : tagList}})
            tagSet = mongohelper.retrieve(["tagset"], tag_collection)
            tagSet[newTag] = 1
            tag_collection.update({"tag" : "tagid"},\
              {"$set" : {"tagset" : tagSet}})
        else:
            tagSet = mongohelper.retrieve(["tagSet"], tag_collection)
            tagSet[newTag] += 1
            tag_collection.update({"tag" : "tagid"},\
              {"$set" : {"tagset" : tagSet}})
        tagFreq = mongohelper.retrieve(["tagfreq"], tag_collection)
        tagFreq += 1
        tag_collection.update({"tag" : "tagid"},\
            {"$set" : {"tagfreq" : tagFreq}})
