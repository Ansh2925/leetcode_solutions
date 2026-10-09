class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n

        def rotateArr(left, right) -> None:
            while left < right:
                nums[right], nums[left] = nums[left], nums[right]
                left +=1
                right -=1

        rotateArr(0, n-1)
        rotateArr(0, k-1)
        rotateArr(k, n-1)    

        return nums     