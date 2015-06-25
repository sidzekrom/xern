from pymongo import *
from base_class import *


connection = MongoClient() 
'''
edit this by giving MongoClient()
an appropriate argument for the database address on the server
'''


''' creates a collection named 'xernbase' and assigns the variable
xern_database to the created database '''
xern_database = connection.get_database('xernbase')

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
        user_collection.update({"User" : userID}, updateDict)

<<<<<<< HEAD

    ''' this adds the general global dictionary of 
    tags to the collection tag_collection'''
=======
    '''
    updateTag : string -> void
    Requires : Nothing
    Ensures : updates the globalTag so that newTag
              is stored as a user accessible tag
    '''
    def updateTag(self, newTag):
        newTag = stringJoin(newTag.split(" "))
        if (not (newTag in retrieve("tagSet", "tag"))):
            tagList = retrieve("tagList", "tag").append(newTag)
            tag_collection.update({"Tag" : "TagID"},\
            {"$set" : {"tagList" : tagList}})
            tagSet = retrieve("tagSet", "tag")
            tagSet[newTag] = 1
            tag_collection.update({"Tag" : "TagID"},\
              {"$set" : {"tagSet" : tagSet}})
        elif(newTag in self.tagSet):
            tagSet = retrieve("tagSet", "tag")
            tagSet[newTag] += 1
            tag_collection.update({"Tag" : "TagID"},\
              {"$set" : {"tagSet" : tagSet}})
>>>>>>> 3478fcda87ad474789812da0ebd0b13ad399a09d

    ''' updates tag information updateTag is a dictionary of the form
        {'$set' : {'title' : '*name*'; 'frequency':*x*} }'''
