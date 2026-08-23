class Solution:
    def findMin(self, nums: List[int]) -> int:
        tgt = float('inf')

        for i in range(len(nums)):
            tgt = min(tgt, nums[i])

        return tgt