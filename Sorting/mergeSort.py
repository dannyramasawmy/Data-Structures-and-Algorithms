# a nicer implementation
def mergeSort(array):
    """
    mergesort
    O(n log n) - time complexity
    O(n) - space complexity
    """
    # base case
    if len(array) <= 1:
        return array

    # get midpoint
    midpoint = len(array)//2

    # split left and right half of array call recursively
    left = mergeSort(array[:midpoint])
    right = mergeSort(array[midpoint:])
    return merge(left, right)


def merge(left, right):
    """Merge two sorted arrays"""

    result = []
    leftPointer = rightPointer = 0

    # when there are elements in both arrays
    while leftPointer < len(left) and rightPointer < len(right):
        # which array has the biggest element
        if left[leftPointer] < right[rightPointer]:
            result.append(left[leftPointer])
            leftPointer += 1
        else: 
            result.append(right[rightPointer])
            rightPointer += 1

    # append the ends
    result.extend(left[leftPointer:])
    result.extend(right[rightPointer:])

    return result


sequence = [3, 6, 1, 5, 3, 6,4, 234, 0, -4, -45, 8, 29, 1, 93, 4.5]
print(f'Merge-sort {mergeSort(sequence)}')

