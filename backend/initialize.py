from tagVector import *
import sys

globalTagData = open('globalTag.txt', 'r+')

tagSize = globalTagData.readline()
sizeTagStrings = int(tagSize)

tagStrings = []
tagStringSet = {}

def stringJoin(ar):
	if len(ar)==1:
		return ar[0]
	elif len(ar)>1:
		return ar[0]+"_"+stringJoin(ar[1:])

for i in range(sizeTagStrings):
    stringOnLine = (globalTagData.readline()).split(" ")
    #the line read contains a tag and the number of times it
    #has been typed in
    stringParse = stringJoin(stringOnLine[0:len(stringOnLine)-1])
    tagStringSet[stringParse] = int(stringOnLine[len(stringOnLine)-1])
    tagStrings.append(stringOnLine[0])

globeoftag = globalTag(tagStrings, sizeTagStrings, tagStringSet)
globalTagData.close()

globeoftag.update("Mehul_Mehul")
globeoftag.update("Mehul")
globeoftag.update("sjfng")
globeoftag.update("Mehul Mehul-Mehul")
globeoftag.update("Preetham Ravi Preethamdeesan")
globeoftag.update("sid")
