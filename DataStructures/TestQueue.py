from Queue import Queue

def test(func, name):
    if func:
        print(f'Test {name} : Pass')
    else:
        print(f'Test {name} : Fail')


def testEnqueue():
    try:
        queue = Queue()
        for idx in range(0, 10):
            queue.enqueue(idx)
            assert str(queue) == str(list(range(0, idx+1)))
        return True
    except:
        return False


def testDequeue():
    try:
        queue = Queue()
        # make queue
        for idx in range(0, 10):
            queue.enqueue(idx)
        # pop from queue
        for idx in range(0, 10):
            assert str(queue) == str(list(range(idx, 10)))
            assert queue.dequeue() == idx
            assert str(queue) == str(list(range(idx+1, 10)))
        return True
    except:
        return False


def testPeek():
    try:
        queue = Queue()
        for idx in range(0, 10):
            queue.enqueue(idx)
            assert queue.peek() == 0
        return True
    except:
        return False


def testLen():
    try:
        queue = Queue()
        for idx in range(0, 10):
            queue.enqueue(idx)
            assert len(queue) == idx + 1
        return True
    except:
        return False


if __name__ == "__main__":
    print(10*'--')
    test(testEnqueue(),     'add item')
    test(testPeek(),        'peek at 1st item')
    test(testDequeue(),     'remove item')
    test(testLen(),         'length')
    print(10*'--')
