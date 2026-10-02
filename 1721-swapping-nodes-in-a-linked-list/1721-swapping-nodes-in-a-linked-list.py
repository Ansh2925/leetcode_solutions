# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head.next:
            return head
            
        nums = []
        
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next

        i = k -1
        j = len(nums)-k

        nums[i], nums[j] = nums[j], nums[i]

        curr = head
        i = 0

        while curr:
            curr.val = nums[i]
            i +=1 
            curr = curr.next

        return head
