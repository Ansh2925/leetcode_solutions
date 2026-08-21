class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        for key, value in freq.items():
            if value == 1:
                return s.index(key)

        return -1
