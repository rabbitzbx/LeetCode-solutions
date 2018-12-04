class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        obj = {}
        arr = []

        for s in strs:
            t = ''.join(sorted(s))
            if t in obj:
                obj[t].append(s)
            else:
                obj[t] = [s]

        for s in obj:
            arr.append(obj[s])

        return arr
