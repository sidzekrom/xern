from database_management import *
from tagVector import *

class locationAction:
    #this adds a new location to the location database.
    #locList specifies the hierarchy (eg. [CMU, Gates, Floor 6, Asian Room])
    def addLocation(self, locList):
        existCheck = location_collection.find_one({'locality' : locList[0]})
        if (existCheck == None):
            existCheck = {'locality' : locList[0], 'locations' : {}}
            location_collection.insert(existCheck)
        locInEx = existCheck['locations']
        for i in range(1, len(locList)):
            if (locList[i] not in locInEx):
                locInEx[locList[i]]['children'] = []
            locInEx[locList[i]] = {'parent' : locList[i-1]}
            locInEx[locList[i-1]]['children'].append(locList[i])
        location_collection.update('locality' : locList[0], {'$set' :\
            {'locations' : locInEx})
