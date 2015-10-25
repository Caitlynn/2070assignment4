'''
Created on 19 Oct 2015
@:author: Caitlynn Zhou
'''

import sys
import pagerefgen
import doublyLinkedList

#take the arguments to generate page reference list as global variable
pages = pagerefgen.generate(int(sys.argv[1]),int(sys.argv[2]))
print('page reference list: ' + str(pages))
'''
class LRU uses LRU algorithms to run referencing pages and replace pages if there is a page fault
'''
class lru(doublyLinkedList.LinkedList):
    def __init__(self, nframe):
        self.nframe = nframe

    '''
    the main function to reference pages and replace pages if there is a page fault
    @:param: none
    @:return: none
    '''
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
    '''
    this function checks if the node is in the frames
    @:param: frames-- a linked list; node: the node that needs to be check in the linked list
    @:return: the node index if found or False if not
    '''
    def checkNode(self,frames, node):
        nodeindex = frames.find(node)
        if nodeindex:
            return nodeindex
        return False
    '''
    this function remove the page from the list then add it to the end of the list
    @:param: frames: a linked list structure; nodeindex: the node that needs to move to the end of the list
    @:return: frames
    '''
    def swap(self,frames,nodeindex):
        tmp = frames._getNode(nodeindex) #tmp = the node we found
        frames.remove(nodeindex) #delete the node from the linkedlist
        frames.add(100,tmp) #then add it to the end of the list
        return frames
    '''
    this function removes the first element of the linked list then add the element to the last of the linked list
    @:param: mypage: the linked list; node: the node that needs to be added to the end of the list
    @:return: mypage
    '''
    def pagefault(self, mypage, node):
        mypage.remove(0) #remove the first element of the list
        mypage.add(100,node) #add the node to the end of the frame
        return mypage

class Clock():
    '''
    the initialisation function of class Clock, nframe is the number of frames, pagedict is a dictionaries that contains [page: index],
    pointer is the pointer to present where in the list is referencing a page, clock list is a list of lists with nframes length and
    has pages and flags in it, page fault is the counter of the page fault.
    @:param: nframe
    @:return: none
    '''
    def __init__(self,nframe):
        self.nframe = nframe
        self.pagedict = {}  #a dictionary to hold page number and the index of the page number in the list or none if the page is not there
        self.pointer = 0
        self.clockList = []
        self.pagefault = 0

    '''
    this function runs to reference pages and replace page if there is a page fault
    @:param: none
    @:return: none
    '''
    def referencePages(self):
        for i in range (self.nframe):
            self.clockList.append([-1,0]) # append [page,flag]

        for i in range (len(pages)):
            if self.pointer >= self.nframe: # set pointer back to 0 if it's bigger than nframe
                self.pointer = 0

            if self.checkPage(pages[i]) == None: #page is not found
                self.processPageFault(pages[i])
            else:
                index = self.checkPage(pages[i])
                self.clockList[index][1] = 1

            print('clock list: ' + str(self.clockList))
            print('current referecing page: ' + str(pages[i]))
        print('page fault: ' + str(self.pagefault))


    '''
    this function handles a pagefault
    @:param: page -- referencing page
    @:return: none
    '''
    def processPageFault(self, page):
        if self.list_not_full(): #if the list is not full then add page to the pointer position
            self.clockList[self.pointer][0] = page
            self.clockList[self.pointer][1] = 1
            self.pagedict[page] = self.pointer #add the new data to the dictionary
            self.pointer += 1

        elif self.clockList[self.pointer][1] == 0: # the list is full but the pointer position flag is 0
            self.pagefault += 1
            self.pagedict[self.clockList[self.pointer][0]] = None # delete the node from the dictionary
            self.clockList[self.pointer][0] = page #set the new data
            self.pagedict[page] = self.pointer #add new index to the dictionary
            self.clockList[self.pointer][1] = 1 #flag = 1
            self.pointer += 1

        elif self.clockList[self.pointer][1] == 1: #if the list is full and current flag is 1
            self.clockList[self.pointer][1] = 0 #set the current flag to 0
            self.pointer += 1 #move to next one
            self.pagedict[page] = None # delete this one from the dictionary

            while True: #loop to find the flag 0
                if self.pointer >= len(self.clockList): #reset pointer if it's bigger than the length of the clock list
                    self.pointer = 0
                if self.clockList[self.pointer][1] == 0: # flag 0 found
                    self.pagefault += 1
                    self.pagedict[self.clockList[self.pointer][0]] = None # delete the current one from the dictionary
                    self.clockList[self.pointer][0] = page #add the page to the list
                    self.pagedict[page] = self.pointer #add the data to the dictionary
                    self.clockList[self.pointer][1] = 1 #flag =1
                    return #break
                elif self.clockList[self.pointer][1] == 1: #flag is not found
                    self.clockList[self.pointer][1] = 0
                    self.pointer += 1 #move to next one
    '''
    this function returns a boolean of if the list if full -- checking if there is still -1 in the list
    @:param: none
    @:return: boolean representing if the list is full
    '''
    def list_not_full(self):
        for i in range (len(self.clockList)):
            if self.clockList[i][0] == -1:
                return True
        return False

    '''
    this function returns the result of checking the input in the dictionary
    @:param: page
    @:return: index if it's found, otherwise returns none
    '''
    def checkPage(self, page):
        if self.pagedict.get(page):
            return self.pagedict.get(page)
        return None


if __name__ == "__main__":
    #alg1 = lru(5)
    #alg1.referencePage()
    alg2 = Clock(5)
    alg2.referencePages()

