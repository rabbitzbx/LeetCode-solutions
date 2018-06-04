class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 初始 prefix 为第一个 str,即 prefix = str[0]
        # 从数组第二个位置开始遍历数组，比较 prefix 和 str 得到新的 prefix
        # 当 prefix 为空时即可返回结果，否则遍历结束后可返回结果
        if not len(strs):
            return ''

        prefix = strs[0]
        for str in strs[1:]:
            tmp = ''
            for i in range(min(len(prefix), len(str))):
                if prefix[i] == str[i]:
                    tmp += prefix[i]
                else:
                    break
            prefix = tmp
            if not len(prefix):
                return prefix

        return prefix

                
