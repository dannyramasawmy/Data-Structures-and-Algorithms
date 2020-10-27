# ===========================================================
#   CLASSES
# ===========================================================

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
        """
        Initialise as an empty list.
        """
        self.head = None
        self.length = 0

    def addHead(self, value):
        """
        addHead - add Node to the start of the list. 
        """
        self.length += 1
        newNode = Node(value)
        # empty list
        if self.head == None:
            self.head = newNode
        # not empty
        else:
            pointer = self.head
            self.head, self.head.next = newNode, pointer

    def addTail(self, value):
        """
        addTail - add Node to the end of the list.
        """
        self.length += 1
        newNode = Node(value)
        # empty list
        if self.head == None:
            self.head = newNode
        # not empty
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = newNode

    def find(self, value):
        """
        find - finds the first item in the list matching value and returns the index and node
        """
        pointer = self.head
        counter = 0
        while pointer:
            if pointer.value == value:
                return (counter, pointer)
            pointer = pointer.next
            counter += 1
        return None

    @staticmethod
    def toLinkedList(items : list):
        """
        toLinkedList - converts a python list to linked list
        """
        linkedList = LinkedList()
        for item in items:
            linkedList.addTail(item)
        return linkedList

    def __getitem__(self, index):
        """
        __getitem__ - index the linked list and return the node
        """
        pointer = self.head
        counter = 0
        while pointer:
            if index == counter:
                return pointer
            counter += 1
            pointer = pointer.next
        raise IndexError('Out of range.')

    def __repr__(self):
        """
        __repr__ - String representation.
        """
        strRepr = ''
        pointer = self.head
        while pointer:
            strRepr += f' {pointer}'
            pointer = pointer.next
        return strRepr + ' None'

    def __len__(self):
        """
        __len__ - the length of the list.
        """
        return self.length


# ===========================================================
#   TEST FUNCTIONS
# ===========================================================


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
        assert myList.length == i+1
    assert f'{myList}' == " 3 -> 2 -> 1 -> 0 -> None"
    # check with dunder method
    assert myList.length == len(myList)

    # create a list add to the tail
    myList = LinkedList()
    for i in range(4):
        myList.addTail(i)
        assert myList.length == i+1
    assert f'{myList}' == " 0 -> 1 -> 2 -> 3 -> None"
    # check with dunder method
    assert myList.length == len(myList)

    # check indexing
    myList = LinkedList()
    for i in range(4):
        myList.addTail(i)
        assert myList[i].value == i

    # change a node in the linked list    
    myList[2].value = 7
    assert f'{myList}' == " 0 -> 1 -> 7 -> 3 -> None"

    # check find
    myList = LinkedList()
    for i in 'alsjdonfkle':
        myList.addTail(i)
    assert f"{myList.find('e')}" == "(10, e ->)"
    assert f"{myList.find('l')}" == "(1, l ->)"
    assert f"{myList.find('z')}" == "None"

    # check linked list
    myList = LinkedList.toLinkedList([0, 1, 2, 3])
    assert f'{myList}' == " 0 -> 1 -> 2 -> 3 -> None"
    
    myList = LinkedList.toLinkedList([0, 'a', 7, 3])
    assert f'{myList}' == " 0 -> a -> 7 -> 3 -> None"

# ===========================================================
#   MAIN PROGRAM
# ===========================================================
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
