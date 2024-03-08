class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n==0:
            return True
        count=0
        for i in range(0,len(flowerbed)):
            l=(i==0) or (flowerbed[i-1]==0)
            r=(i==len(flowerbed)-1) or (flowerbed[i+1]==0)
            if flowerbed[i]==0 and l and r:
                flowerbed[i]=1
                count+=1
        if count>=n:
          return True
        
        return False

