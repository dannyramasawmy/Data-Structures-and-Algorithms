def binarySearch(sortedArray, value):
    """
    binary search, iterative
    O(log n) - time complexity
    """
    # left and right pointers
    left = 0
    right = len(sortedArray) - 1

    while left <= right:
        # find the mid point
        mid = (right + left) // 2
        # correct value
        if sortedArray[mid] == value:
            return mid
        # search left half
        elif sortedArray[mid] > value:
            right = mid - 1
        # search right half
        else: 
            left = mid + 1
    return None
            

# initialize a sorted array
array = list(range(-10,10))
print(array)
# if the item is not in the array
index = binarySearch(array, 3.3)
print(f'Non-existent item -> {array[index] if index else index}')
# item is in the array
index = binarySearch(array, 7)
print(f'Existing item -> {array[index] if index else index}')




