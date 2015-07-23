from database_management import *
from tagVector import *

class locationAction:
    #this adds a new location to the location database.
    #locList specifies the hierarchy (eg. [CMU, Gates, Floor 6, Asian Room])
    #was thinking that following line should be
    #addlocation(loclist, parentid = -1). Thoughts, Praful?
    def addLocation(self, locList, parentid):
        if (location_collection.find_one({'_id' : 'count'}) == None):
            location_collection.insert({'_id' : 'count', 'entries' : 0})
        prevDict = {}
        if (parentid == -1):
            prevDict = {'_id' : -1}
        else:
            prevDict = location_collection.find_one({'_id' : parentid})
        for i in range(len(locList)):
            nextEntry = mongohelper.retrieve(['entries'],\
                location_collection, to_search = {'_id' : 'count'})
            dictToAdd = {'_id' : nextEntry, 'name' : locList[i],\
                'parent' : prevDict['_id'], 'children' : []}
            location_collection.insert(dictToAdd)
            location_collection.update({'_id' : 'count'},\
                {'$set' : {'entries' : nextEntry + 1}})
            if (prevDict['_id'] != -1):
                location_collection.update({'_id' :\
                    prevDict['_id']}, {'$push' : {'children' : nextEntry}})
            prevDict = dictToAdd
