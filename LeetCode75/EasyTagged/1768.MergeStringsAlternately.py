class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = []
        minIdx = min(len(word1),len(word2))

        for i in range(minIdx) :
            res.append(word1[i])
            res.append(word2[i])
        
        res.append(word2[minIdx:])
        res.append(word1[minIdx:])
        res = "".join(res)
        return res

        
