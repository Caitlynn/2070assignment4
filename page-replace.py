__author__ = 'Caitlynn'
import sys
import pagerefgen
import doublyLinkedList
from itertools import cycle

        #take the arguments to generate page reference list
pages = pagerefgen.generate(int(sys.argv[1]),int(sys.argv[2]))
print(pages)
class lru(doublyLinkedList.LinkedList):
    def __init__(self, nframe):
        self.nframe = nframe

    def createPage(self):
        mypage = doublyLinkedList.LinkedList()
        for i in range (self.nframe):
            mypage.add(100,pages.pop(0))  #add the ith element in pages list to the end of the linked list
        for i in range (mypage.get_size()):
            print(mypage._getNode(i).data)

        for i in range (len(pages)):
            if mypage.get_size() == 0:
                mypage.add(pages[i])
            else:
                nodeindex = self.checkNode(mypage, pages[i])
                if nodeindex:
                    self.swap(mypage, nodeindex)
                else:
                    self.pagefault(mypage, pages[i])


    def checkNode(self,frames, node):
        nodeindex = frames.fine(node)
        if nodeindex:
            return nodeindex
        return False

    def swap(self,frames,nodeindex):
        tmp = frames._getNode(nodeindex) #tmp = the node we found
        frames.remove(nodeindex) #delete the node from the linkedlist
        frames.add(100,tmp) #then add it to the end of the list
        return frames

    def pagefault(self, mypage, node):
        mypage.remove(0) #remove the first element of the list
        mypage.add(100,node) #add the node to the end of the frame
        return mypage


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