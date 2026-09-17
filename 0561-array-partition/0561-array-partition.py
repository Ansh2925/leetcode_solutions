class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        nums.sort()

        for i in range(0, n, 2):
            res += min(nums[i], nums[i+1])

        return res