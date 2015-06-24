from pymongo import *
from base_class import *

connection = MongoClient() 
'''
edit this by giving MongoClient()
an appropriate argument for the database address on the server
'''

''' creates a collection named 'userbase' and assigns the variable
user_database to the created database '''
user_database = connection.get_database('userbase')

''' creates a collection named 'userCollection' and assigns the variable
user_collection to the created collection '''
user_collection = user_database.userCollection


class userActions:    
    ''' this class defines actions that can
       be performed on the user database '''
    
    def __init__(self):
        self.usercount = 0
        self.userDict = {}

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

