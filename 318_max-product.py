class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        maxNum = 0;
        flags = [];
        for i, word in enumerate(words):
            flags.append([sum(1 << (ord(c) - 97) for c in set(word)), len(words[i])])            
        for i in range(len(words)):
            for j in range(i, len(words)):
                if not flags[i][0] & flags[j][0]:
                    maxNum = max(maxNum, flags[i][1] * flags[j][1])
        return maxNum

