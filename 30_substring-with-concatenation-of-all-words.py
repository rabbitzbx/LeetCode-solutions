class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not len(words):
            return []

        result = []
        total = {}
        wordLen = len(words[0])

        for word in words:
            total[word] = total[word] + 1 if word in total else 1

        for i in range(wordLen):
            index = i
            current = {}
            currentNum = 0

            for j in range(i, len(s), wordLen):
                word = s[j: j + wordLen]
                if word in total:
                    currentNum += 1
                    current[word] = current[word] + 1 if word in current else 1

                    if current[word] > total[word]:
                        firstPass = False
                        while not firstPass:
                            startWord = s[index: index + wordLen]
                            current[startWord] -= 1
                            currentNum -= 1
                            index += wordLen
                            if startWord == word:
                                firstPass = True
                    elif currentNum == len(words):
                        result.append(index)
                        current[s[index: index + wordLen]] -= 1
                        currentNum -= 1
                        index += wordLen
                else:
                    index = j + wordLen
                    current = {}
                    currentNum = 0

        return result
