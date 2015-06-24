''' a file of helper functions that will generally aid in mundane activities of other files '''

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
    distance norms: here are a bunch of distance metrics that will be tested
    for effectiveness in recommendation systems and the best one will be
    chosen: some are standard metrics (like Euclidean and Manhattan/Taxicab)
    and some are based on ad-hoc heuristics.
    A suitable threshold will be determined.

    Notes : Euclidean and Manhattan would return a short distance if the
            vectors are close enough but the problem arises when they are
            close in dimensions where their values are similar but distant
            in a dimension where the user might have a high value.
            maxMin seems most plausible because users generally require
            only one of their interests to be represented at an event
            in order to go. If there exists a dimension where
            both the user and the event are above a threshold increases
            the likelihood of a user going to the event. However, there
            is a mild issue when the user is likely to go to an event but
            maxMin is lower than the threshold.
    maxMin exceeds threshold => recommended. Otherwise, switch to other norms
    '''

    '''
    euclidean : (tagVector * tagVector) -> float
    requires : vector1 and vector2 are valid vectors
    ensures : returns the euclidean distance between the two
              tag vectors
    '''
def euclidean(vector1, vector2):
	euclidAcc = 0
	for i in range(self.size):
		euclidAcc += (vector1.retrieve(self.tagStrings[i])\
		- vector2.retrieve(self.tagStrings[i])) ** 2
	return euclidAcc ** 0.5

    '''
    manhattan : (tagVector * tagVector) -> float
    requires : vector1 and vector2 are 2 valid vectors
    ensures: returns the Manhattan distance between the two
             tag vectors (M(v1, v2) = (v11-v21) + ... + (v1n-v2n))
    '''
def manhattan(vector1, vector2):
	manhattanAcc = 0
	for i in range(self.size):
		manhattanAcc += (vector1.retrieve(self.tagStrings[i]) -
		vector2.retrieve(self.tagStrings[i]))
	return manhattanAcc

    '''
    maxMin : (tagVector * tagVector) -> float
    requires : vector1 and vector2 are valid vectors
    ensures : for each dimension i, take the minimum of vector1[i]
              and vector2[i] and take the maximum across all
              dimensions
    '''
def maxMin(vector1, vector2):
	maxMinAcc = 0
	for i in range(self.size):
		maxMinAcc = max(maxMinAcc, min(vector1[i], vector2[i]))