class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        low = 0
        mid = 1

        n = len(nums)

        while low < n and mid < n:

            if nums[low] % 2 == 0:
                low += 2

            elif nums[mid] % 2 == 1:
                mid += 2

            else:
                nums[low], nums[mid] = nums[mid], nums[low]

                low += 2
                mid += 2

        return nums