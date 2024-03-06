# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre=None
        temp=head
        while(temp):
            nextNode=temp.next
            temp.next=pre
            pre=temp
            temp=nextNode
        head=pre
        return head
