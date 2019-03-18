# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i = 0
        copy = intervals[:]

        for interval in copy:
            s0, s1, e0, e1 = interval.start, newInterval.start, interval.end, newInterval.end
            if e1 < s0:
                intervals.insert(i, newInterval)
                return intervals
            if e1 <= e0:
                intervals[i] = Interval(min(s0, s1), e0)
                return intervals
            if s1 > e0:
                i += 1
                continue
            intervals.pop(i)
            newInterval = Interval(min(s0, s1), e1)

        intervals.append(newInterval)

        return intervals
