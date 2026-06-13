class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        def atMost(k):
            freq = {}
            l = 0
            count = 0
            for h in range(len(nums)):
                freq[nums[h]] = freq.get(nums[h], 0) + 1
                while len(freq) > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1
                count += h - l + 1
            return count

        K = len(set(nums))
        return atMost(K) - atMost(K - 1)