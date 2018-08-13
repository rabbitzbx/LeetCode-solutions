class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return self.helper(s, ['(', ')'])

    def helper(self, s, pars):
        results = ['']
        stack = 0

        for c in s:
            # 每个 result 加上当前的字符
            for i, item in enumerate(results):
                results[i] = item + c
            if c == pars[0]:
                stack += 1
            if c == pars[1]:
                stack -= 1
            # stack 小于 0 时需要删除任意一个 pars[1]
            if stack < 0:
                arr = []
                for i, item in enumerate(results):
                    arr = arr + self.remove(item, pars[1])
                results = list(set(arr))
                stack = 0
        
        if (stack > 0):
            arr = []
            for item in results:
                arr = arr + self.helper(item[::-1], [')', '('])
            for i, item in enumerate(arr):
                arr[i] = item[::-1]
            return arr

        return results

    # remove pars[1]
    def remove(self, s, flag):
        arr = []
        for i, c in enumerate(s):
            if c == flag:
                arr.append(s[:i] + s[i + 1:])
        return arr
