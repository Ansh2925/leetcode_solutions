class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
            n = len(nums)
            sets = 1 << n
            res = []

            for num in range(sets):
                lst = []
                for i in range(n):
                    if num & (1 << i) != 0:
                        lst.append(nums[i])
                res.append(lst)
            return res