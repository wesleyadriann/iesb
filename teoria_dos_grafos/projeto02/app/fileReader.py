
# -*- coding: utf-8 -*-

def fileReader():
    dataFile = open('dados.txt', "r")
    data = dataFile.read()
    dataFile.close()
    data = data.split('\n')
    return data
