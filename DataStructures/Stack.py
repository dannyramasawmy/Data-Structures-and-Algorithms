class Stack:
    """
    Stack class.
    """
    def __init__(self):
        """
        init - Initialise empty stack.
        """
        self.items = []

    def __len__(self):
        """
        len - get the length
        """
        return len(self.items)

    def peek(self):
        """
        peek - see the end value
        """
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return None

    def push(self, value):
        """
        push - push items to the stack
        """
        self.items.append(value)

    def pop(self):
        """
        pop -  pop items from stack
        """
        return self.items.pop()

    def __repr__(self):
        return f'{self.items}'

