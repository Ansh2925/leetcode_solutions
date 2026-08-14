class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = {}
        max_len = 0
        left = 0

        for i in range(len(s)):
            
            freq[s[i]] = freq.get(s[i], 0) + 1

            while freq[s[i]] > 2:
                freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, i - left + 1)

        return max_len     