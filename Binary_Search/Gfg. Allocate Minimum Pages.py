class Solution:
    def findPages(self, arr, k):
        n = len(arr)

        if k > n:
            return -1

        low = max(arr)
        high = sum(arr)

        def can_allocate(max_pages):
            students = 1
            pages = 0

            for book in arr:
                if pages + book <= max_pages:
                    pages += book
                else:
                    students += 1
                    pages = book

                    if students > k:
                        return False

            return True

        while low <= high:
            mid = (low + high) // 2

            if can_allocate(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low
