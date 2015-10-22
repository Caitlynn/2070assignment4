__author__ = 'Caitlynn'
import sys
import pagerefgen
import doublyLinkedList
from itertools import cycle

pages = pagerefgen.generate(int(sys.argv[1]),int(sys.argv[2]))
print(pages)
class lru(doublyLinkedList.LinkedList):
    def __init__(self, nframe):
        self.nframe = nframe
        self.npage = len(pages)

    def createPage(self):
        #pages = []
        #pages = pagerefgen.generate(int(sys.argv[1]), int(sys.argv[[2]]))
        #take the arguments to generate page reference list
        mypage = doublyLinkedList.LinkedList()

        if len(pages) >= self.nframe:
            for i in range (self.nframe):
                mypage.add(i, pages[i]) #add nframe number of pages to the frame
        else:
            for i in range (self.npage):
                mypage.add(i, pages[i]) #add npage number of pages to the frame if there's less pages than frames
        print(mypage.get_size())
'''
        for i in range (self.npage):
            pagedict = {pages[i] : mypage._getNode(i).data}
        print(pagedict)
'''

if __name__ == "__main__":
    alg1 = lru(5)
    alg1.createPage()
'''
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
'''