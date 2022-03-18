

def quicksort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot - 1)
        quicksort(arr, pivot + 1, right)


def partition(arr, left, right):
    # set pivot as the last num
    pivot = arr[right]

    # create a variable to track the largest index of numbers lower than the defined
    leftwall = left - 1
    for i in range(left, right):
        if arr[i] <= pivot:
            leftwall += 1
            swap(arr, i, leftwall)

    # put pivot in the middle
    swap(arr, right, leftwall + 1)
    return leftwall + 1


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp 