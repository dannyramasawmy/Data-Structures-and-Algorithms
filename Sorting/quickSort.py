def quickSort(a, l, r):

    if l >= r:
        return a

    x = a[l]
    i = l
    j = r

    while i <= j:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1
        if i <= j:
            t = a[i]
            a[i] = a[j]
            a[j] = t
            i += 1
            j -= 1

    
    quickSort(a, l, j)
    quickSort(a, i, r)


    return a


# quicksort between bounds
a = [5, 2, 1, 7, 5, 3, 2, 3]
l = 0
r = 3
print(f'Quicksort {quickSort(a, l, r)}')


###################################
def quickSort2(array):
    """Quicksort for whole array"""
    if len(array) <= 1:
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

    return quickSort2(itemsLower) + [pivot] + quickSort2(itemsGreater)

a = [5, 2, 1, 7, 5, 3, 2, 3]
print(f'Quicksort {quickSort2(a)}')
