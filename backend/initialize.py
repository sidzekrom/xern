from tagVector import *
import sys

globalTagData = open('globalTag.txt', 'r+')

tagSize = globalTagData.readline()
sizeTagStrings = int(tagSize)

tagStrings = []
tagStringSet = {}

for i in range(sizeTagStrings):
    stringOnLine = (globalTagData.readline()).split(" ")
    #the line read contains a tag and the number of times it
    #has been typed in
    stringParse = stringOnLine[0]
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
