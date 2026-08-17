class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        low = 0
        high = n-1

        while low <= high:
            if nums[high] == val:
                high -= 1
            elif nums[low] == val:
                nums[low], nums[high] = nums[high], nums[low]
                low +=1
                high -=1
            else:
                low +=1

        return low

