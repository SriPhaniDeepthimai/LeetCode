class Solution(object):
    def __init__(self):
        self.a=0
        self.b=0

    def Gcd(self,a,b):
        if (b==0):
            return a
        else:
            return self.Gcd(b,a%b)
    def gcdOfStrings(self, str1, str2):

        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if (str1+str2)==(str2+str1):
            length=self.Gcd(len(str1),len(str2))
            return str1[0:length]
        else:
            return""
        
        
