def bisect_left(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid].end < x.start:
            lo = mid+1
        else:
            hi = mid
    return lo


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        s = bisect_left(intervals, newInterval)
        intervals.insert(s, newInterval)

        while s < len(intervals)-1:
            if intervals[s].end >= intervals[s+1].start:
                intervals[s].start = min(
                    intervals[s].start, intervals[s+1].start)
                intervals[s].end = max(intervals[s].end, intervals[s+1].end)
                del intervals[s+1]
            else:
                break

        return intervals
