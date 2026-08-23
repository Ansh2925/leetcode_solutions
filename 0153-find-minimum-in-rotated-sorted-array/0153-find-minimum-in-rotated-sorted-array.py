class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1
        tgt = float(inf)

        while low <= high:
            mid = (low+high)//2

            tgt = min(tgt, nums[mid])

            if nums[mid] >= nums[high]:
                low = mid +1
            else:
                high = mid -1

        return tgt