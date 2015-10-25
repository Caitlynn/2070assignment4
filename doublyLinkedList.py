'''
Created on 19 Oct 2015
@:author: Caitlynn Zhou
'''

'''
class Node is for creating a node and setting the next node and previous node, and also it can get data of the input node
'''
class Node(object):
    '''
        Initialization function for class Node
        @:param: a node
        @:return: none
    '''
    def __init__(self, d, n = None, p = None):
        self.data = d
        self.next_node = n
        self.prev_node = p
    '''
    get next function returns the next node of the current node
    @:param: none
    @:return: next node
    '''
    def get_next(self):
        return self.next_node
    '''
    set_next function set the input node as next node of the current node
    @:param: n which is the next node
    @:return: none
    '''
    def set_next(self,n):
        self.next_node = n
    '''
    get next function returns the previous node of the input node
    @:param: none
    @:return: previous node
    '''
    def get_prev(self):
        return self.prev_node
    '''
    set_prev function set the input node as previous node of the current node
    @:param: p which is the previous node
    @:return: none
    '''
    def set_prev(self,p):
        self.prev_node = p
    '''
    get data function returns the data of the current node
    @:param: none
    @:return: the data of the current node
    '''
    def get_data(self):
        return self.data
    '''
    set_data function set the input data to the current node
    @:param: d which is the data that's going to be set to the current node
    @:return: none
    '''
    def set_data(self,d):
        self.data = d

'''
class LinkedList is a doubly linked list structure, it has appending function, check empty function,get size function, deletion function and find node function
'''
class LinkedList(object):
    '''
        Initialization function for class LinkedList
        @:param: root of the linkedlist set to none
        @:return: none
    '''
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    '''
    get size function returns the size of the linked list
    @:param: none
    @:return: the size of the linked list
    '''
    def get_size(self):
        return self.size
    '''
    is_empty function returns a boolean if the linked list is empty
    @:param: none
    @:return: a boolean to show if the linked list is empty
    '''
    def is_empty(self):
        return self.size == 0
    '''
    get node function returns the node of the input index of the linked list
    @:param: index of the node that user wants to get
    @:return: the node of the input index
    '''
    def _getNode(self,index):
        node = self.root
        for _ in range(index):
            node = node.get_next()
        return node
    '''
    add function add an item to index position in the linked list
    @:param: index the position user want to add, item
    @:return: none
    '''

    def add(self,index, item):
        if index < 0:
            index = 0
        elif index > self.size:
            index = self.size

        if index == 0:
            self.root = Node(item, self.root, None)
        else:
            node = self._getNode(index-1)
            node.next_node = Node(item, node.next_node, node)
        self.size += 1
    '''
    remove function remove the input index node from the linked list by connect the previous node to the next node of the deletion node
    @:param: index of the deletion node
    @:return: none
    '''
    def remove(self,index):
        if self.is_empty():
            raise IndexError("list is empty")
        if index < 0 or index >= self.size:
            raise IndexError("index is out of range")
        if index == 0:
            self.root = self.root.get_next()
            self.root.set_prev(None)
        else:
            node = self._getNode(index)
            next = node.get_next()
            prev = node.get_prev()
            if next:
                next.set_prev(prev)
            if prev:
                prev.set_next(next)
        self.size -= 1
    '''
    find function checks the input node in the linked list and return the index of the node
    @:param: d -- a node
    @:return: the index of the node if found, None is the node is not found.

    '''
    def find(self,d):
        this_node = self.root
        i = 0
        while this_node:
            if this_node.get_data() == d:
                return i
            else:
                this_node = this_node.get_next()
                i += 1
        return None

if __name__ == "__main__":
    myList = LinkedList()
    myList.add(0,5)
    myList.add(1,23)
    myList.add(2,2)
    myList.add(3,7)
    myList.add(4,50)
    for i in range (myList.size):
        print(myList._getNode(i).data)
    print("\n")
    myList.remove(0)
    for i in range (myList.size):
        print(myList._getNode(i).data)