###################################
def quickSort(array):
    """
    Quicksort
    O(n log n) - average time, O(n**2) worst
    O(n) - space (naive) 
    """
    if len(array) <= 1:
        # base case
        return array

    # get middle element
    pivot = array.pop(len(array)//2)

    # create left and right list
    itemsGreater = []
    itemsLower = []

    for item in array:
        if item > pivot:
            itemsGreater.append(item)
        else:
            itemsLower.append(item)

    return quickSort(itemsLower) + [pivot] + quickSort(itemsGreater)

a = [5, 2, 1, 7, 5, 3, 2, 3]
print(f'Quicksort {quickSort(a)}')
