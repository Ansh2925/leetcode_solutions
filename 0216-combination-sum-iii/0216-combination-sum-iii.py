class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        result = []

        def backtrack(idx, Sum, subset):

            if Sum == n:
                if len(subset) == k:
                    result.append(subset.copy())
                    return
                return
            if idx >= len(nums):
                return

            subset.append(nums[idx])
            Sum += nums[idx]
            backtrack(idx +1, Sum, subset)

            e = subset.pop()
            Sum -= e
            backtrack(idx +1, Sum, subset)

        
        backtrack(0, 0, [])

        return result