class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        
        for i in range(n):
            sum = 0
            j = 0
            while j <= i:
                sum += nums[j]
                j+=1
            result.append(sum)

        return result
            