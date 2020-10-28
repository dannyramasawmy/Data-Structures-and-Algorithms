def selectionSort(array):
    """
    Selection sort.
    O(n**2) - time complexity
    O(1) - space complexity
    """
    for currentDx in range(len(array)):
        comparisonDx = currentDx + 1
        swapDx = currentDx
        while comparisonDx < len(array):
            # find the smallest element
            if array[comparisonDx] < array[swapDx]:
                swapDx = comparisonDx
            comparisonDx += 1            
        # swap elements
        array[currentDx], array[swapDx] = array[swapDx], array[currentDx]

    return array

array = [1,4,2,8,3,5,0,8,3,2,8,7,-3,-5,-1]
print(selectionSort(array))