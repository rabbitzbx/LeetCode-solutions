class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        candidates.sort()
    
        helper(candidates, target, 0, results, [])
    
        return results

def helper(arr, remain, index, results, result):
    if remain < 0:
        return

    if remain == 0:
        results.append(result)
        return

    for i in range(index, len(arr)):
        num = arr[i]
        tmp = result[:]
        tmp.append(num)
        
        helper(arr, remain - num, i, results, tmp) 

