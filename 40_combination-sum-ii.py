class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.results = []
        candidates.sort()

        self.helper(candidates, target, [])

        return self.results

    def helper(self, arr, target, result):
        if target < 0:
            return

        if target == 0:
            self.results.append(result)
            return

        for i, num in enumerate(arr):
            if i == 0 or num != arr[i-1]:
                self.helper(arr[i+1:], target - num, result + [num])
