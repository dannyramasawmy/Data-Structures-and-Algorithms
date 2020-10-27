def bubbleSort(items):
    """Bubble sort"""
    def swap(firstIndex, secondIndex):
        temp = items[firstIndex]
        items[firstIndex] = items[secondIndex]
        items[secondIndex] = temp

    # loop for each element
    for idx in range(len(items)):
        jdx = 0
        stop = len(items) - idx
        while jdx < stop - 1:
            # swap if larger
            if items[jdx] > items[jdx + 1]:
                swap(jdx, jdx + 1)
            jdx += 1
    return items

a = [3,2,5,1,8,3,9,23,5,12,42,9,7,0,-3,-2,4,-4]
print(bubbleSort(a))

