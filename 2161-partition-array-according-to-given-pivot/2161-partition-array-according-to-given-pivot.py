class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less_than_pivot = []
        greater_than_pivot = []
        pivot_lst = []

        for i in range(len(nums)):
            if nums[i] < pivot:
                less_than_pivot.append(nums[i])
            
            if nums[i] > pivot:
                greater_than_pivot.append(nums[i])

            if nums[i] == pivot:
                pivot_lst.append(nums[i])


        less_than_pivot.extend(pivot_lst)
        less_than_pivot.extend(greater_than_pivot)

        return less_than_pivot