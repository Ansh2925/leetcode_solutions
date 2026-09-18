class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        even = []
        odd = []
        res = []
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                odd.append(nums[i])
            else:
                even.append(nums[i])
        i = 0
        j = 0
        k = 0
        while k < len(nums):
            if k % 2 != 0:
                res.append(odd[i])
                i += 1
            else:
                res.append(even[j])
                j += 1

            k +=1

        return res 