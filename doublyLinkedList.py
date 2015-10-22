__author__ = 'Caitlynn'
class Node(object):
    def __init__(self, d, n = None, p = None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def get_next(self):
        return self.next_node
    def set_next(self,n):
        self.next_node = n
    def get_prev(self):
        return self.prev_node
    def set_prev(self,p):
        self.prev_node = p
    def get_data(self):
        return self.data
    def set_data(self,d):
        self.data = d

class LinkedList(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    def get_size(self):
        return self.size
    def is_empty(self):
        return self.size == 0
    def _getNode(self,index):
        node = self.root
        for _ in range(index):
            node = node.get_next()
        return node

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

    def find(self,d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
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