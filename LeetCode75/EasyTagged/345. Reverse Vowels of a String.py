class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels="AEIOUaeiou"
        l=list(s)
        i=0
        j=len(l)-1
        while(i<j):
            while i<j and l[i] not in vowels:
                i+=1
            while i<j and l[j] not in vowels:
                j-=1
            l[i],l[j]=l[j],l[i]
            i+=1
            j-=1
        return "".join(l)

        
