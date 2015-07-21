import numpy as np
from pymongo import *

'''
tagvector is a class that contains information related to the weight
assigned to each tag for a user it contains a dictionary that maps tags
to the weights for each user for the tag
'''
class tagVector:
    '''
    getValue : (string, string) -> float
    requires : the input string is a valid tag in the global database
    ensures: retrieve returns the value associated with the specific
             tag by returning the value attached to the tag
             in the dictionary of the user
    '''
    def getValue(self, tag, user):
        usersTags = mongohelper.retrieve(['tags'], user_collection,\
        toSearch = {'user' : user})
        if (tag in usersTags):
            return usersTags[tag]
        else:
            return 0.0

    '''
    measureSimMin : (string, string) -> float
    The two input strings are valid users. The distance between their vectors
    is measured and a float value of the result is returned. The maxmin norm
    is used
    '''
    def measureSimMin(self, vector1, v1tot, vector2, v2tot):
        vector1tags = list(vector.keys())
        acc = 0
        for tag in vector1tags:
            acc = max(acc, min(float(vector1[tag])/\
                float(v1tot), float(vector2[tag)/\
                float(v2tot)))
        return acc

    '''
    measureSimCos : (string, string) -> float
    Input strings are valid usernames. Distance between vectors is measured
    by normalized dot product
    '''
    def measureSimCos(self, vector1, v1tot, vector2, v2tot):
        v1tags = list(vector1.keys())
        acc = 0
        for tag in v1tags:
            acc += vector1[tag] * vector2[tag]
        return float(acc) / ((float(v1tot) ** 0.5) * (float(v2tot)\
            ** 0.5))

    #the next task within this file would be to generalize the getValue
    #function to locations and events
