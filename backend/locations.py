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
    
    #more about the location data structure here.
    #each location is represented as a document of the following format.
    #{'_id' : 1, 'name' : 'CMU', 'parent' : -1, 'children : [1, 6, 12, 14, 15],
    #'tags' : {tech : 87, CS : 100, Math : 84, Putnam : 78, Design : 86,
    #Architecture : 81, Engineering : 82, Food : 76}}
    #or
    #{'_id' : 3, 'name' : 'Floor 6', 'parent' : 2, 'children' : [4, 5], tags :{
    #CS : 100, Free Food : 99, Math : 80, Biology : 12}}
    #the '_id' field lets you identify a location by a unique numeric ID (which
    #I simply set as n for the n-th location added).
    #1 is CMU, 2 is Gates, 3 is floor 6, 4 is Asian room, 5 is Ada's office
    #the way we look up a place and get info is through it's ID.
    #if location A is contained in location B, then B > A
    #And if B > A and there is no C such that B > C > A, then B is the parent
    #of A and A is a child of B. In other words, A should be immediately
    #contained in B.

