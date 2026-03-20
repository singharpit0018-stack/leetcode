class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
            
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        curr_interval = intervals[0]
        
        for i in range(1, len(intervals)):
            next_interval = intervals[i]
            
            if curr_interval[1] >= next_interval[0]:
                curr_interval[1] = max(curr_interval[1], next_interval[1])
            else:
                merged.append(curr_interval)
                curr_interval = next_interval
        
        merged.append(curr_interval)
        
        return merged