class Solution:
    cache = ["1"]

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n - 1 < len(self.cache):
            return self.cache[n - 1]

        for i in range(len(self.cache), n):
            last = self.cache[i - 1]
            current = ''
            count = 1
            for j in range(1, len(last) + 1):
                if j == len(last) or last[j] != last[j - 1]:
                    current += str(count)
                    current += last[j - 1]
                    count = 1
                else:
                    count += 1
            self.cache.append(current)

        return self.cache[-1]
