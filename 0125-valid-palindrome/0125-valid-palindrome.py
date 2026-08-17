class Solution:
    def isPalindrome(self, s: str) -> bool:
        simple = []

        for ch in s:
            if ch.isalnum():
                simple.append(ch.lower())

        return simple == simple[::-1]