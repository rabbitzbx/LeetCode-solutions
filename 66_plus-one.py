class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 计算 digits[i] + 1，若结果为 10，digits[i] 更新为 0，重复该步骤（i 从 n 开始递减）。
        # 若 i 为 0，在 list 开头添加一个值为 1 的元素, 并退出计算。
        # 若结果小于 10，digits[i] 更新为 digits[i] + 1, 并退出计算。
        digits = self.helper(digits, len(digits) - 1)
        return digits

    def helper(self, digits, i):
        tmp = digits[i] + 1
        if tmp == 10:
            digits[i] = 0
            if i == 0:
                digits = [1] + digits
            else:
                digits = self.helper(digits, i - 1)
        else:
            digits[i] = tmp
        return digits