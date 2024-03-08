class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        k=list(s.split())
        k=k[::-1]
        return " ".join(k)

        
