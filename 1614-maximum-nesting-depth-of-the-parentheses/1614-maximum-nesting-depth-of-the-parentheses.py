class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        m = 0
        for ch in s:
            if ch == '(':
                count += 1
            if ch == ')':
                count -= 1 
            m = max(m, count)

        return m