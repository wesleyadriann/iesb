
# -*- coding: utf-8 -*-

def fileReader(filePath):
    dataFile = open(filePath, "r")
    data = dataFile.read()
    dataFile.close()
    data = data.split('\n')
    return data