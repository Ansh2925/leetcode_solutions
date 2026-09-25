class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(min(28, len(nums))):
            total = 0
            while nums[i] > 0:
                total += nums[i] % 10
                nums[i] = nums[i] // 10
            if total == i:
                return i
        return -1