



def merge_sort(array):
    n = len(array)
    mid = n // 2
    if n == 1:
        return array
    
    left_arr = merge_sort(array[:mid])
    right_arr = merge_sort(array[mid:])
    result = merge(left_arr, right_arr)
    return result


def merge(left_arr, right_arr):

    i = left = right = 0
    len1 = len(left_arr)
    len2 = len(right_arr)
    result = [0 for _ in range(len1 + len2)]

    # Do comparisons and fill result array until we reach the end of either left or right
    while left < len1 and right < len2:
        if left_arr[left] <= right_arr[right]:
            result[i] = left_arr[left]
            i += 1
            left += 1
        else:
            result[i] = right_arr[right]
            i += 1
            right += 1

    # Fill array with remaining nums in left array
    while left < len1:
        result[i] = left_arr[left]
        i += 1
        left += 1
    # Fill array with remaining nums in right array
    while right < len2:
        result[i] = right_arr[right]
        i += 1
        right += 1
    # arrays are merged and sorted
    return result 

