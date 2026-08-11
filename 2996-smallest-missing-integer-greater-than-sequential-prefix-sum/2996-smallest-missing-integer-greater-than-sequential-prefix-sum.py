class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                sum += nums[i]
            else:
                break

        for j in range(0, len(nums)):
            if sum in nums:
                sum +=1
                # j = 0
        return sum