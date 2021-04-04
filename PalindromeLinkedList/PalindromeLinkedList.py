# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast: # odd case 121
            slow = slow.next 
        
        fast = head
        slow = self.reverse(slow)
        
        while slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
    
    def reverse(self, head: ListNode):
        pre = None
        while head:
            next = head.next
            head.next = pre
            # move forward
            pre = head
            head = next
        return pre
            
# T: O(N)
# S = O(1)