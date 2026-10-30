class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []

        def backtrack(idx, total, subset):

            if total == target:
                result.append(subset.copy())
                return

            if total > target or idx >= len(candidates):
                return

            # Include current element
            subset.append(candidates[idx])
            backtrack(idx + 1, total + candidates[idx], subset)
            subset.pop()

            # Exclude current element
            next_idx = idx + 1

            # Skip duplicate elements
            while next_idx < len(candidates) and candidates[next_idx] == candidates[idx]:
                next_idx += 1

            backtrack(next_idx, total, subset)

        backtrack(0, 0, [])
        return result