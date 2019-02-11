# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        if not len(intervals):
            return []

        intervals = sorted(intervals, key=lambda item: item.start)
        result = [intervals[0]]

        for item in intervals[1:]:
            if item.start > result[-1].end:
                result.append(item)
            else:
                result[-1].end = max(result[-1].end, item.end)

        return result
