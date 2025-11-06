# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Put the value in a stack
        if head==None:
            return head 
        if head.next==None:
            return head
        stack = []

        while head != None:
            stack.append(head.val)
            head = head.next
        
        reversed = ListNode(stack.pop())
        
        pointer = reversed
        while stack:
            pointer.next = ListNode(stack.pop())
            pointer = pointer.next
        return reversed
if __name__ == "__main__":
    sol = Solution()
    # Create a linked list 1->2->3->4->5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    reversed_head = sol.reverseList(head)
    # Print reversed linked list
    current = reversed_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")