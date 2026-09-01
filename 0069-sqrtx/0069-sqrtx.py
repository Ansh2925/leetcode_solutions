class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        low = 0
        high = x
        ans = 0

        while low <= high:
            mid = low + (high -low)//2

            if mid <= x//mid:
                ans = mid
                low = mid +1
            else:
                high = mid -1

        return ans