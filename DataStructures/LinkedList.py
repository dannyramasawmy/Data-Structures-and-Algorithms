# ===========================================================
#   CLASSES FOR LINKED LIST
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
