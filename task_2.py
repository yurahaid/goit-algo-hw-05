def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iter = 0
    upper_bound = None

    while left <= right:
        iter += 1
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return iter, arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]

    return iter, upper_bound