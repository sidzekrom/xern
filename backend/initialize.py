from *.py import *
import sys

globalTagData = open('globalTag.txt', 'r+')

tagVectorData = globalTagData.readline()
tagStrings = tagVectorData.split(" ")
sizeTagStrings = len(tagStrings)

globeoftag = globalTag(tagStrings, sizeTagStrings)
