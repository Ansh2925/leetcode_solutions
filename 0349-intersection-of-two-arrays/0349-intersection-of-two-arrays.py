class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2= set(nums2)

        nums1 = list(nums1)
        nums2 = list(nums2)
        res = []
        if len(nums1) > len(nums2):
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    res.append(nums2[i])
        else:
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    res.append(nums1[i])

        return res