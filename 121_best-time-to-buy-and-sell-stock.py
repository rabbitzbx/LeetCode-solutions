class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not len(prices):
            return 0

        result = 0
        minPrice = prices[0]

        for price in prices:
            minPrice = min(price, minPrice)
            result = max(result, price - minPrice)

        return result
