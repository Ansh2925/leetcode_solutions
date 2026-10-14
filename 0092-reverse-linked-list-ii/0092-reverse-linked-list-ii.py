# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head

        # if dummy.next is None:
        #     return None

        temp = dummy
        for _ in range(left-1):
            temp = temp.next

        left_ptr = temp.next
        curr = left_ptr
        prev = None

        for _ in range(right-left+1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        temp.next = prev
        left_ptr.next = curr

        return dummy.next
        

