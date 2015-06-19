from pymongo import *

connection = MongoClient() '''edit this by giving MongoClient()
                              an appropriate argument for the database
                              address on the server'''

connection.get_database('userbase')

class userActions:
    '''this class defines actions that can
       be performed on the user database '''
    def __init__(self):
        self.usercount = 0
        self.userDict = {}
    ''' '''
    def addUser(self, userID, userDict):
        self.usercount += 1
        self.userDict[userID] = userDict

