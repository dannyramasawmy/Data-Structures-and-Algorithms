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

    def delete(self, index):
        """
        delete - delete node at a specified index
        """
        # get the node
        node = self[index]
        self.length -= 1
        # end / front of list
        if node.next == None:
            if index > 0:
                node = self[index-1]
                node.next = None
            else:
                self.head = None
        # general case
        else:
            node.value = node.next.value
            node.next = node.next.next

    def pop(self, index='end'):
        """
        pop - returns node breaks pointer, removes item from the list
        """
        if index == 'end':
            index = self.length - 1
            # 0 length list
            if index < 0:
                return None
        # make a copy
        returnNode = Node(self[index].value)
        self.delete(index)
        return returnNode

    def reverse(self):
        """
        reverse - reverses the linked list
        """
        # initialize
        dragger, current, runner = None, None, self.head
        while runner:
            dragger = current
            current = runner
            runner = runner.next
            current.next = dragger
        self.head = current

    @staticmethod
    def toLinkedList(items: list):
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
    try:
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

        return True
    except:
        return False


def testAddHead():
    try:
        # create a list add to the head
        myList = LinkedList()
        for i in range(4):
            myList.addHead(i)
            assert myList.length == i+1
        assert f'{myList}' == " 3 -> 2 -> 1 -> 0 -> None"
        # check with dunder method
        assert myList.length == len(myList)

        return True
    except:
        return False


def testAddTail():
    try:
        # create a list add to the tail
        myList = LinkedList()
        for i in range(4):
            myList.addTail(i)
            assert myList.length == i+1
        assert f'{myList}' == " 0 -> 1 -> 2 -> 3 -> None"
        # check with dunder method
        assert myList.length == len(myList)

        return True
    except:
        return False


def testGetItem():
    try:
        # check indexing
        myList = LinkedList()
        for i in range(4):
            myList.addTail(i)
            assert myList[i].value == i

        # change a node in the linked list
        myList[2].value = 7
        assert f'{myList}' == " 0 -> 1 -> 7 -> 3 -> None"

        return True
    except:
        return False


def testFind():
    try:
        # check find
        myList = LinkedList()
        for i in 'alsjdonfkle':
            myList.addTail(i)
        assert f"{myList.find('e')}" == "(10, e ->)"
        assert f"{myList.find('l')}" == "(1, l ->)"
        assert f"{myList.find('z')}" == "None"

        return True
    except:
        return False


def testListConvert():
    try:
        # check method for creating lists
        myList = LinkedList.toLinkedList([0, 1, 2, 3])
        assert f'{myList}' == " 0 -> 1 -> 2 -> 3 -> None"
        myList = LinkedList.toLinkedList([0, 'a', 7, 3])
        assert f'{myList}' == " 0 -> a -> 7 -> 3 -> None"

        return True
    except:
        return False


def testReverseList():
    try:
        # check reversing lists
        myList = LinkedList.toLinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8])
        myList2 = LinkedList.toLinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8])
        myRevList = LinkedList.toLinkedList([8, 7, 6, 5, 4, 3, 2, 1, 0])
        myList.reverse()
        assert f'{myList}' == f'{myRevList}'
        myList.reverse()
        assert f'{myList}' == f'{myList2}'

        return True
    except:
        return False


def testDeleteItems():
    try:
        myList = LinkedList.toLinkedList([0, 1, 2, 3, 4, 5])
        assert f'{myList}' == f'{LinkedList.toLinkedList([0,1,2,3,4,5])}'
        myList.delete(5)
        assert f'{myList}' == f'{LinkedList.toLinkedList([0,1,2,3,4])}'
        myList.delete(0)
        assert f'{myList}' == f'{LinkedList.toLinkedList([1,2,3,4])}'
        myList.delete(2)
        assert f'{myList}' == f'{LinkedList.toLinkedList([1,2,4])}'
        myList.delete(2)
        myList.delete(0)
        assert f'{myList}' == f'{LinkedList.toLinkedList([2])}'
        myList.delete(0)
        assert f'{myList}' == f'{LinkedList.toLinkedList([])}'

        return True
    except:
        return False


def testPop():
    try:
        myList = LinkedList.toLinkedList([0, 1, 2, 3, 4, 5])
        assert f'{myList}' == f'{LinkedList.toLinkedList([0,1,2,3,4,5])}'
        assert f'{myList.pop(5)}' == f'{Node(5)}'
        assert f'{myList}' == f'{LinkedList.toLinkedList([0,1,2,3,4])}'
        assert f'{myList.pop(0)}' == f'{Node(0)}'
        assert f'{myList}' == f'{LinkedList.toLinkedList([1,2,3,4])}'
        assert f'{myList.pop(2)}' == f'{Node(3)}'
        assert f'{myList}' == f'{LinkedList.toLinkedList([1,2,4])}'
        assert f'{myList.pop()}' == f'{Node(4)}'
        assert f'{myList}' == f'{LinkedList.toLinkedList([1,2])}'
        assert f'{myList.pop()}' == f'{Node(2)}'
        assert f'{myList}' == f'{LinkedList.toLinkedList([1])}'
        assert f'{myList.pop()}' == f'{Node(1)}'
        assert f'{myList}' == f'{LinkedList.toLinkedList([])}'
        assert f'{myList.pop()}' == f'{None}'
        assert f'{myList}' == f'{LinkedList.toLinkedList([])}'

        return True
    except:
        return False


def test(func, name):
    if func:
        print(f'Test {name} : Pass')
    else:
        print(f'Test {name} : Fail')


# ===========================================================
#   MAIN PROGRAM
# ===========================================================
if __name__ == "__main__":
    # test node
    print(10*'--')

    test(testNode(),        'node class')
    test(testAddHead(),     'add at head')
    test(testAddTail(),     'add at tail')
    test(testGetItem(),     'get the item')
    test(testFind(),        'find a node')
    test(testListConvert(), 'convert list to linked list')
    test(testReverseList(), 'reverse list')
    test(testDeleteItems(), 'delete item in list')
    test(testPop(),         'pop item from list')
    print(10*'--')
