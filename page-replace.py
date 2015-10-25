__author__ = 'Caitlynn'
import sys
import pagerefgen
import doublyLinkedList

#take the arguments to generate page reference list
pages = pagerefgen.generate(int(sys.argv[1]),int(sys.argv[2]))
print(pages)
class lru(doublyLinkedList.LinkedList):
    def __init__(self, nframe):
        self.nframe = nframe

    def referencePage(self):
        mypage = doublyLinkedList.LinkedList()
        printstring = ''
        for i in range (len(pages)):
            if mypage.get_size() < self.nframe: # when the frame is not filled
                nodeindex = self.checkNode(mypage,pages[i])
                if nodeindex:
                    self.swap(mypage,nodeindex)
                else:
                    mypage.add(100,pages[i])
            else: # when the frame is filled
                nodeindex = self.checkNode(mypage, pages[i]) # check if the node is already referenced
                if nodeindex:
                    self.swap(mypage, nodeindex)
                else:
                    self.pagefault(mypage, pages[i])
            for i in range (mypage.get_size()):
                printstring += str(mypage._getNode(i).data)
                print(printstring)

    def checkNode(self,frames, node):
        nodeindex = frames.find(node)
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

class Clock():
    def __init__(self,nframe):
        self.nframe = nframe
        self.pagedict = {}  #a dictionary to hold page number and the index of the page number in the list or none if the page is not there
        self.pointer = 0
        self.clockList = []
        self.pagefault = 0

    def referencePages(self):
        for i in range (self.nframe):
            self.clockList.append([-1,0]) # append [page,flag]

        for i in range (len(pages)):
            if self.pointer >= self.nframe:
                self.pointer = 0

            if self.checkPage(pages[i]) == None: #page is not found
                self.processPageFault(pages[i])
            else:
                index = self.checkPage(pages[i])
                self.clockList[index][1] = 1
            print('page reference list: ' + str(pages))
            print('clock list: ' + str(self.clockList))
            print('current referecing page: ' + str(pages[i]))
            print('page fault: ' + str(self.pagefault))


    def processPageFault(self, page):
        self.pagefault += 1
        if self.list_not_full(): #if the list is not full then add page to the pointer position
            self.clockList[self.pointer][0] = page
            self.clockList[self.pointer][1] = 1
            self.pagedict[page] = self.pointer
            self.pointer += 1

        elif self.clockList[self.pointer][1] == 0:
            self.pagedict[self.clockList[self.pointer][0]] = None
            self.clockList[self.pointer][0] = page
            self.pagedict[page] = self.pointer
            self.clockList[self.pointer][1] = 1
            self.pointer += 1

        elif self.clockList[self.pointer][1] == 1:
            self.clockList[self.pointer][1] = 0
            self.pointer += 1
            self.pagedict[page] = None

            while True:
                if self.pointer >= len(self.clockList):
                    self.pointer = 0
                if self.clockList[self.pointer][1] == 0:
                    self.pagedict[self.clockList[self.pointer][0]] = None
                    self.clockList[self.pointer][0] = page
                    self.pagedict[page] = self.pointer
                    self.clockList[self.pointer][1] = 1
                    return
                elif self.clockList[self.pointer][1] == 1:
                    self.pointer += 1

    def list_not_full(self):
        for i in range (len(self.clockList)):
            if self.clockList[i][0] == -1:
                return True
        return False

    def checkPage(self, page):
        if self.pagedict.get(page):
            return self.pagedict.get(page)
        return None


if __name__ == "__main__":
    #alg1 = lru(5)
    #alg1.referencePage()
    alg2 = Clock(5)
    alg2.referencePages()

