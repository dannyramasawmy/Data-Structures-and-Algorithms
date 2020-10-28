from collections import deque

class Queue():
    """
    A queue data structure using a deque object.
    """
    def __init__(self):
        """
        init - Initialise empty queue.
        """
        self.items = deque()

    def __len__(self):
        """
        len - get the length
        """
        return len(self.items)

    def peek(self):
        """
        peek - see the front value
        """
        if len(self.items) > 0:
            return self.items[0]
        else:
            return None

    def enqueue(self, value):
        """
        enqueue - put items at the back of the queue
        """
        self.items.append(value)

    def dequeue(self):
        """
        dequeue -  get items from front of the queue
        """
        return self.items.popleft()

    def __repr__(self):
        return f"[{', '.join(str(i) for i in self.items)}]"

