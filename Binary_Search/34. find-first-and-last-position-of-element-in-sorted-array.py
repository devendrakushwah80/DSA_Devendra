class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        res1 = -1
        res2 = -1

        # Find first occurrence
        l = 0
        h = len(nums) - 1

        while l <= h:
            m = (l + h) // 2

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                h = m - 1
            else:
                res1 = m
                h = m - 1

        res.append(res1)

        # Find last occurrence
        l = 0
        h = len(nums) - 1

        while l <= h:
            m = (l + h) // 2

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                h = m - 1
            else:
                res2 = m
                l = m + 1

        res.append(res2)

        return res
