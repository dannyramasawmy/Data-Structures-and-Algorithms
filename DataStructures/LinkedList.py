class Node():
    """
    Node : a node on the linked list.
    """

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.value} ->'


class LinkedList():
    """
    LinkedList : a linked list with helpful methods.
    """
    def __init__(self):
        self.head = None

    def addHead(self, value):
        """
        addHead - add Node to the start of the list. 
        """
        if self.head == None:
            self.head = Node(value)
        else:
            pointer = self.head
            self.head = Node(value)
            self.head.next = pointer

    def __repr__(self):
        strRepr = ''
        pointer = self.head
        while pointer:
            strRepr += f' {pointer}'
            pointer = pointer.next
        return strRepr + ' None'


def testNode():
    """
    Tests for the node object.
    """

    # simple check initializing a Node
    n1 = Node(4)
    assert n1.value == 4
    assert n1.next == None
    # new Node 
    n2 = Node(5)
    assert n2.value == 5
    assert n2.next == None
    n1.next = n2
    assert n1.next == n2

def testLinkedList():
    """
    Tests linked list.
    """
    # create a list add to the head
    myList = LinkedList()
    for i in range(4):
        myList.addHead(i)
    assert f'{myList}' ==  " 3 -> 2 -> 1 -> 0 -> None"
    



#===========================================================
#   MAIN PROGRAM
#===========================================================

if __name__ == "__main__":
    # test node
    print(10*'--')
    print('Test Node')
    testNode()
    print('Tests passed')
    print(10*'--')

    # test linked list
    print(10*'--')
    print('Test LinkedList')
    testLinkedList()
    print('Tests passed')
    print(10*'--')


