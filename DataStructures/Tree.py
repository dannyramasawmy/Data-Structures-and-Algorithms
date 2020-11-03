class Node():
    """
    Node : a node on the linked list.
    """

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.value} ->'

class BinarySearchTree():
    """
    Binary search tree.
    """
    pass




class Heap():
    """
    Heap min
    """
    def __init__(self):
        """
        Initialise heap
        """
        self.array = []

    def getParentIndex(self, index):
        """
        get the parent index of the child node
        """
        pass

    def insert(self, value):
        """
        insert - add a node to the bottom, bubble the node up the tree
        """
        if self.head == None:
            self.head = Node(value)

    def extract(self):
        """
        extract - take the top element, bubble the node down the tree
        """
        pass

    def peek(self):
        """
        peek - see the min/max of the tree
        """
        return 

    def heapify(self):
        """
        heapify - reorders tree
        """
        pass
