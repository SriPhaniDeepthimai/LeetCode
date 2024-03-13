class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        answer=[]
        res1=[]
        res2=[]
        for i in set(nums1):
            if i not in nums2:
                res1.append(i)
        for i in set(nums2):
            if i not in nums1:
                res2.append(i)
        answer.append(res1)
        answer.append(res2)
        return answer
        
        
        
