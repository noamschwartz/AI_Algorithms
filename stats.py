'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''
import csv
import random
from collections import namedtuple, Counter
from ways import load_map_from_csv

#count number of links
def getLinks(roads):
    result = sum(1 for x in roads.iterlinks())
    return result

def getMaxOut(roads):
    maxi = max(len(x.links) for x in roads.junctions())
    return maxi

def getMinOut(roads):
    mini = min(len(x.links) for x in roads.junctions())
    return mini

def getAvgOut(roads):
    links = sum(len(x.links) for x in roads.junctions())
    junctions = sum(1 for x in roads.junctions())
    return links / junctions

def getMaxLinks(roads):
    maxi = max(x.distance for x in roads.iterlinks())
    return maxi

def getMinLinks(roads):
    mini = min(x.distance for x in roads.iterlinks())
    return mini

def getAvgLinks(roads):
    linkDist = sum(x.distance for x in roads.iterlinks())
    linkSum = sum(1 for x in roads.iterlinks())
    avg = linkDist / linkSum
    return avg

#this creates 100 problems
def createOneHundredJunctions(roads):
    myFile = open('problems.csv', 'w')
    for i in range(0, 100):
        rand = random.randint(0, len(roads.junctions()))
        temp = roads[rand]
        links = temp.links
        j = random.randint(0, len(links)-1)
        sourceTo = str(links[j].source)
        targetTo = str(links[j].target)
        dataToWrite = sourceTo + ',' + targetTo + '\n'
        myFile.write(dataToWrite)


def map_statistics(roads):
    '''return a dictionary containing the desired information
    You can edit this function as you wish'''
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])
    #get number of junctions
    juncNum = len(roads.junctions())

    #create 100 problems
    #createOneHundredJunctions(roads)

    return {
        'Number of junctions' : juncNum,
        'Number of links' : getLinks(roads),
        'Outgoing branching factor' : Stat(max=getMaxOut(roads),
                                          min=getMinOut(roads),
                                          avg=getAvgOut(roads)),
        'Link distance' : Stat(max=getMaxLinks(roads), min=getMinLinks(roads), avg=getAvgLinks(roads)),
        # value should be a dictionary
        # mapping each road_info.TYPE to the no' of links of this type
        'Link type histogram' : Counter(x.highway_type for x in roads.iterlinks()).items(),  # tip: use collections.Counter
    }


def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))

        
if __name__ == '__main__':
    from sys import argv
    assert len(argv) == 1
    print_stats()
