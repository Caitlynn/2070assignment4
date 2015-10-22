__author__ = 'Caitlynn'
import sys
import pagerefgen
import doublyLinkedList
from itertools import cycle

pages = pagerefgen.generate(int(sys.argv[1]),int(sys.argv[2]))
print(pages)
def lru():
    return

def clock():
    pagedict = dict()
    pagedict[page] = index
    clockArray = []
    for index in range (len(pages)):
        clockArray.append(index)
    clockArray = cycle(clockArray) #make the list circular
    for item in clockArray:
        return
    return
