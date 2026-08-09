class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        s = s.strip()
        for ch in s:
            count += 1

            if ch == " ":
                count = 0

        return count 