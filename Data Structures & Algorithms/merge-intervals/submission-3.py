class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
	
        intervals.sort() # default python will look at the first index
        merged = [intervals[0]]
        start1, end1 = intervals[0][0], intervals[0][1]

        for start2, end2 in intervals[1:]:
            if end1 >= start2:
                merged.pop()
                merged.append([start1, max(end1,end2)])
            else:
                merged.append([start2,end2])
            
            start1, end1 = merged[-1]

        return merged
