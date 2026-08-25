class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # nums.sort()

        for i in range(1, 1001):
            if i not in nums:
                if i == k:
                    return k
                if i % k == 0:
                    return i
                
