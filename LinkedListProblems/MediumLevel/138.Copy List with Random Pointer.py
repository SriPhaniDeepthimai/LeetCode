"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        prev=ans=Node(0)
        curr=head
        d=dict()
        while curr:
            prev.next=Node(0)
            prev.next.val=curr.val
            d[curr]=prev.next
            curr=curr.next
            prev=prev.next
        curr=head
        ptr=ans.next
        while curr:
            if curr.random==None:
                ptr.random=None
            else:
                ptr.random=d[curr.random]
            curr=curr.next
            ptr=ptr.next
        return ans.next
        
        """
        :type head: Node
        :rtype: Node
        """
        
