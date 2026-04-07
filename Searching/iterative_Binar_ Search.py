def IBinarySearch(arr,target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 3, 5, 7, 9]
print("Array:", arr)
target = int(input("Enter the target value: "))
result = IBinarySearch(arr, target)
print("Index of {target}:", result if result != -1 else "Not found")