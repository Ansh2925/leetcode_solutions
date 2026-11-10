# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        

        def reverse(head):
            curr = head
            prev = None

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        new_head = reverse(head)

        stack = []
        curr = new_head

        while curr:

            if not stack or stack[-1] <= curr.val:
                stack.append(curr.val)

            curr = curr.next
    
        def create_linked_list(values):
            dummy = ListNode()
            tail = dummy

            for val in values:
                tail.next = ListNode(val)
                tail = tail.next

            return dummy.next

        return reverse(create_linked_list(stack))
