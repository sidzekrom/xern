import numpy as np

'''
globalTag : class with string list, size of string list
            and dictionary with a mapping from tags to ints
'''
class globalTag:
    '''
    __init__ : string list * int * dict -> globalTag class
    Summoned using globalTag(tagStrings,size,tagSet)
    Requires : size = len(tagStrings)
    Ensures : returns a globalTag object with the inputted
              initialized parameters
    '''
    def __init__(self, tagStrings, size, tagSet):
        self.tagStrings = tagStrings
        self.tagSet = tagSet
        self.size = size
    '''
    update : string -> void
    Requires : Nothing
    Ensures : updates the globalTag so that newTag
              is stored as a user accessible tag
    '''
    def update(self, newTag):
        newTag = self.stringJoin(newTag.split(" "))
        if (not (newTag in self.tagSet)):
            self.tagStrings.append(newTag)
            self.tagSet[newTag] = 1
            self.size += 1
        elif(newTag in self.tagSet):
            self.tagSet[newTag] += 1
        globalTagData = open('globalTag.txt', 'w')
        globalTagData.write(str(self.size))
        globalTagData.write('\n')
        for i in range(len(self.tagStrings)):
            toWrite = self.tagStrings[i] + " "\
                + str(self.tagSet[self.tagStrings[i]]) + "\n"
            globalTagData.write(toWrite)
        globalTagData.close()
    '''
    stringJoin : string list -> string
    Requires : input is nonempty
    Ensures : concatenates elements of the list by underscore ("_")
    '''
    def stringJoin(self, listString):
        if (len(listString) == 1):
            return listString[0]
        elif (len(listString) > 1):
            return (listString[0] + "_" + self.stringJoin(listString[1:]))


'''
tagvector is a class that contains information related to the weight
assigned to each tag for a user it contains a dictionary that maps tags
to the weights for each user for the tag
'''
class tagVector:
    '''
    '''
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
