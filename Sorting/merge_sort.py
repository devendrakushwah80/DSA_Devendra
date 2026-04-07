def merge(A, B):
    i, j = 0, 0
    C = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    C.extend(A[i:])
    C.extend(B[j:])
    return C


def mergesort(A):
    if len(A) <= 1:
        return A

    mid = len(A) // 2

    left = mergesort(A[:mid])
    right = mergesort(A[mid:])

    return merge(left, right)

A = [5, 2, 9, 1, 3]
print(mergesort(A))