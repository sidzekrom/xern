import numpy as np

class globalTag:
    def __init__(self, tagStrings, size):
        self.tagStrings = tagStrings
        self.size = size
    def update(self, newTag):
        self.tagStrings.append(newTag)
        self.size += 1


class tagVector:
    '''
    - each dimension is a tag
    - and there is a numerical value along each dimension
    - if a numerical value has not been initialized in a dimension,
      then by default set it to 1/(sqrt(dimension number))
    
    Stuff to figure out:
    - When a new tag is created how do we add it to
      the tag vector of every user?
    - Figure out the math behind normalization etc. for events
    - Representation of tagvectors (storing numpy vector indices
      in a dictionary etc). 
    '''
    def __init__(self):
        self.diction = {}
    def retrieve(tag):
        if (tag in self.diction):
            return self.diction[tag]
        else:
            self.diction[tag] = 1.0 / (float(globalTag.size) ** 0.5)
