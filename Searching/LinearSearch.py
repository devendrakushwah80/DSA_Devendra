# Linear Search Program in Python

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i  
    return -1         


arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter element to search: "))

result = linear_search(arr, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")