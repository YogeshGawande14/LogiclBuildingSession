def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print("Linear Search:", linear_search([10, 20, 30, 40], 30))


def binary_search_iterative(arr, target):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

print("Binary Search Iterative:", binary_search_iterative([1, 3, 5, 7, 9], 7))


def binary_search_recursive(arr, l, r, target):
    if l > r:
        return -1
    mid = (l + r) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid+1, r, target)
    else:
        return binary_search_recursive(arr, l, mid-1, target)

print("Binary Search Recursive:", binary_search_recursive([1, 3, 5, 7, 9], 5, 0, 4))


def first_occurrence(arr, target):
    l = 0
    r = len(arr) - 1
    result = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            result = mid
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return result

print("First Occurrence:", first_occurrence([1, 2, 4, 4, 4, 5, 7], 4))


def last_occurrence(arr, target):
    l = 0
    r = len(arr) - 1
    result = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            result = mid
            l = mid + 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return result

print("Last Occurrence:", last_occurrence([1, 2, 4, 4, 4, 5, 7], 4))
