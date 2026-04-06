def RBinarySearch(arr, low, high, target):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return RBinarySearch(arr, low, mid - 1, target)
    else:
        return RBinarySearch(arr, mid + 1, high, target)
    
arr = [1, 3, 5, 7, 9]
print("Array is : ",arr)
target = int(input("Enter target element to search: "))
result = RBinarySearch(arr, 0, len(arr) - 1, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")