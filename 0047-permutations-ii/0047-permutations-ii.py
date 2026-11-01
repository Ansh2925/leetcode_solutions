class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(idx):

            if idx == len(nums):
                if nums[:] not in result:
                    result.append(nums[:])
                return

            for i in range(idx, len(nums)):

                nums[idx], nums[i] = nums[i], nums[idx]

                backtrack(idx +1)

                nums[idx], nums[i] = nums[i], nums[idx]


        backtrack(0)

        return result