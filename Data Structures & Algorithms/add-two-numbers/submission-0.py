# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = s2 = ""
        
        # reverse l1
        prev, curr = None, l1
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head1 = prev

        # reverse l2
        pre, cur = None, l2
        while cur:
            nx = cur.next
            cur.next = pre
            pre = cur
            cur = nx
        head2 = pre

        # append strings

        while head1:
            s1 += str(head1.val)
            head1 = head1.next

        while head2:
            s2 += str(head2.val)
            head2 = head2.next

        res = int(s1) + int(s2)

        # create new linked list
        dummy = ListNode(0)
        tail = dummy
        for c in str(res)[::-1]:
            tail.next = ListNode(int(c))
            tail = tail.next

        return dummy.next