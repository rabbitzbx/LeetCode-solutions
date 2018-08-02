class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 分两种情况：
        # 匹配字母(或者.)。若匹配，则继续(s=s[1:],p=p[1:])。若不匹配，则返回结果 return False
        # 匹配字母(或者.)加上*。若匹配，则继续(s=s[1:] p=p 或者 s=s p=p[2:])。若不匹配，则继续(s=s p=p[2:])
        self.cache = {}
        return self.match(s, p)
    
    def match(self, s, p):
        n = len(s)
        m = len(p)
        if n in self.cache and m in self.cache[n]:
            return self.cache[n][m]
        if not n and not m:
            return True
        if not m:
            return False
        tmp = n and (p[0] == s[0] or p[0] == '.')
        if m == 1:
            if n == 1 and tmp:
                return True
            return False
        if p[1] != '*':
            if tmp:
                return self.helper(s[1:], p[1:])
            return False
        if tmp:
            return self.helper(s, p[2:]) or self.helper(s[1:], p)
        return self.helper(s, p[2:])

    def helper(self, s, p):
        n = len(s)
        m = len(p)
        if n not in self.cache:
            self.cache[n] = {}
        self.cache[n][m] = self.match(s, p)
        return self.cache[n][m]

