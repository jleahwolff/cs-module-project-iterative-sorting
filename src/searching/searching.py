def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if (arr[i] == target):
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    left = target -1
    right = target + 1
    # Your code here
    if right >= left:
        mid = left + (right - 1)

        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            return binary_search(arr, left, mid-1, target)
        
        else:
            return binary_search(arr, mid + 1, right, target)

    else:
        return - 1


