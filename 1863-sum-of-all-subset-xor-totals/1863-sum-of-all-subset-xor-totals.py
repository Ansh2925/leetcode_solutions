class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:

        result = []
        def backtrack(idx, subset):
            
            if idx >= len(nums):
                if len(subset.copy()) >= 1:
                    result.append(subset.copy())
                    return
                return 

            subset.append(nums[idx])
                
            backtrack(idx +1, subset)
            subset.pop()
            backtrack(idx +1, subset)

        backtrack(0, [])
        
        Sum = 0
        for row in result:
            res = 0
            for num in row:
                res ^= num
            Sum += res

        return Sum


