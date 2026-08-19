class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = 0
        reversed_list = digits[::-1]
        for i in range(len(reversed_list)):
            integer += reversed_list[i]*(10**i)

        integer += 1

        return [int(digit) for digit in str(integer)]