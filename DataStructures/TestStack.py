from Stack import Stack

def test(func, name):
    if func:
        print(f'Test {name} : Pass')
    else:
        print(f'Test {name} : Fail')


def testPush():
    try:
        stack = Stack()
        for idx in range(0, 10):
            stack.push(idx)
            assert str(stack) == str(list(range(0, idx+1)))
        return True
    except:
        return False


def testPop():
    try:
        stack = Stack()
        # make stack
        for idx in range(0, 10):
            stack.push(idx)
        # pop from stack
        for idx in range(9, -1, -1):
            assert stack.pop() == idx
            assert str(stack) == str(list(range(0, idx)))

        return True
    except:
        return False


def testPeek():
    try:
        stack = Stack()
        for idx in range(0, 10):
            stack.push(idx)
            assert stack.peek() == idx
        return True
    except:
        return False


def testLen():
    try:
        stack = Stack()
        for idx in range(0, 10):
            stack.push(idx)
            assert len(stack) == idx + 1
        return True
    except:
        return False


if __name__ == "__main__":
    print(10*'--')
    test(testPush(),        'push item')
    test(testPeek(),        'peek item')
    test(testPop(),         'peek item')
    test(testLen(),         'length')
    print(10*'--')
