# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        
        dummy = ListNode(0)
        dummy.next = head

        if head is None:
            return head

        nums = []
        curr = dummy.next
        while curr:
            nums.append(curr.val)
            curr = curr.next

        n = len(nums)
        k = k % n

        def rotate(left, right) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1
                right -=1

        rotate(0, n-1)
        rotate(0, k-1)
        rotate(k, n-1)

        i = 0
        curr = dummy.next
        while curr and i < n:
            curr.val = nums[i]
            i += 1
            curr = curr.next


        return dummy.next