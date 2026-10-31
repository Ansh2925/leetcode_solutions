class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        nums = []
        result = []
        for i in range(1, n+1):
            nums.append(i)

        def backtrack(idx, subset):
            if idx >= len(nums):
                if len(subset) == k:
                    result.append(subset.copy())
                return

            subset.append(nums[idx])
            backtrack(idx+1, subset)
            subset.pop() 
            backtrack(idx+1, subset)


        backtrack(0, [])

        return result
