class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=[]
        for i in s:
            if i!="*":
                l.append(i)
            else:
                l.pop()
        return "".join(l)
