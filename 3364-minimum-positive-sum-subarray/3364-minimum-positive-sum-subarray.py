class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        
        Min = float('inf')
        def min_sum(nums, k):
            window_sum = sum(nums[:k])
            min_sum = float('inf')

            if window_sum > 0:
                min_sum = window_sum

            for i in range(k, len(nums)):
                window_sum += nums[i]
                window_sum -= nums[i-k]

                if window_sum > 0:
                    min_sum = min(min_sum, window_sum)

            return min_sum

        for i in range(l, r+1):

            Min = min(Min, min_sum(nums, i))

        return -1 if Min == float('inf') else Min