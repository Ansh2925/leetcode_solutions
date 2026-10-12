class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        sets = 1 << len(nums)
        res = []

        for num in range(sets):
            lst = []
            for i in range(len(nums)):
                if num & (1<<i) != 0:
                    lst.append(nums[i])
            res.append(lst)

        result = []
        for lst in res:
            if lst not in result:
                result.append(lst)

        return result 