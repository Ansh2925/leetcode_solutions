class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            digit_sum = sum(map(int, str(nums[i])))
            if i == digit_sum:
                return i
                
        return -1