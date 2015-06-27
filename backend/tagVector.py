import numpy as np
from pymongo import *

'''
tagvector is a class that contains information related to the weight
assigned to each tag for a user it contains a dictionary that maps tags
to the weights for each user for the tag
'''
class tagVector:
    '''
    __init__, summoned using tagVector() initializes an empty
    dictionary through tagVector().
    '''
    def __init__(self):
        self.diction = {}
    
    '''
    retrieve : string -> float
    requires : the input string is a valid tag in the global database
    ensures: retrieve returns the value associated with the specific
             tag by returning the value attached to the tag
             in the dictionary
    '''
    def retrieve(tag):
        if (tag in self.diction):
            return self.diction[tag]
        else:
            self.diction[tag] = 1.0 / (float(globalTag.size) ** 0.5)
            return self.diction[tag]

    
