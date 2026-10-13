class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) -1
        high = 0
        while i <= j:
            area = min(height[i], height[j])*(j-i)
            high = max(high, area)

            if height[i] < height[j]:
                i +=1
            else:
                j -=1
        return high