# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0)
        dummy.next=head
        temp1=dummy
        temp2=dummy
        for i in range(0,n):
            temp1=temp1.next
        while(temp1.next!=None):
            temp2=temp2.next
            temp1=temp1.next
        temp2.next=temp2.next.next

        return dummy.next

        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
