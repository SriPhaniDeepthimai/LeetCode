class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        j=0
        res=[]
        for i in range(len(candies)):
            if candies[j]+extraCandies>=max(candies):
                res.append(True)
            else:
                res.append(False)
            j+=1
        return res
        
