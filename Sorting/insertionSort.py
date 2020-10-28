def insertionSort(array):
    """
    insertion sort

    """
    idx = 1
    while idx < len(array):
        x = array[idx]
        jdx = idx - 1
        # shift the elements along
        while jdx >= 0 and array[jdx] > x:
            array[jdx+1] = array[jdx]
            jdx = jdx - 1
        # insert the element
        array[jdx+1] = x
        idx = idx + 1
    return array


array = [1,4,2,8,3,5,0,8,3,2,8,7,-3,-5,-1]
# array = [1,4,2,-5,-1]

print(insertionSort(array))