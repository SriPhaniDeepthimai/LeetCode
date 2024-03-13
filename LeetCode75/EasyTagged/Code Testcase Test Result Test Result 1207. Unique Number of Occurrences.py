class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        res=[]
        for i in set(arr):
            ans=arr.count(i)
            res.append(ans)
        res1=set(res)
        if len(res1)==len(res):
            return True
        else:
            return False
        
