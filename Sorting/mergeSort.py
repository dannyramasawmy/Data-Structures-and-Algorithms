def mergeSort(sequence):
    def merge(sequence, left, middle, right):

        result = []

        i = left
        j = middle
        while i < middle and j < right:
            if sequence[i] < sequence[j]:
                result.append(sequence[i])
                i += 1
            else:
                result.append(sequence[j])
                j += 1

        while i < middle:
            result.append(sequence[i])
            i += 1

        while j < right:
            result.append(sequence[j])
            j += 1

        for i in range(left, right):
            sequence[i] = result[i - left]

    def split(sequence, left, right):
        middle = (left + right) // 2

        if left == middle: return
        split(sequence, left, middle)
        split(sequence, middle, right)
        merge(sequence, left, middle, right)

    split(sequence, 0, len(sequence))

    return sequence


sequence = [3, 6, 1, 5, 3, 6]
print(f'Merge {mergeSort(sequence)}')


# a nicer implementation
def mergeSort2(array):
    """If length == 1"""
    if len(array) <= 1:
        return array

    # get midpoint
    midpoint = len(array)//2

    # split left and right half of array call recursively
    left = mergeSort2(array[:midpoint])
    right = mergeSort(array[midpoint:])

    return merge(left, right)

def merge(left, right):
    """Merge two sub arrays"""

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


sequence = [3, 6, 1, 5, 3, 6]
print(f'Merge2 {mergeSort2(sequence)}')

