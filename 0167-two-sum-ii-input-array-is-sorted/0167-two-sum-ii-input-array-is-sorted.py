class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        res = []
        i = 0
        j = len(numbers)-1
        while i < j:
            total = numbers[i] + numbers[j]
            if total == target:
                res.append(i +1)
                res.append(j +1)
                break
            elif total < target:
                i += 1
            else:
                j -= 1

            # i += 1
            # j -= 1


        return res