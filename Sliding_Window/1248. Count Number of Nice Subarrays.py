class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def atMost(k):
            l = 0
            count = 0
            odd_count = 0
            for h in range(len(nums)):
                if nums[h] % 2 == 1:
                    odd_count += 1
                while odd_count > k:
                    if nums[l] % 2 == 1:
                        odd_count -= 1
                    l += 1
                count += h - l + 1
            return count
        return atMost(k) - atMost(k - 1)