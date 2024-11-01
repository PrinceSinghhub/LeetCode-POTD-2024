class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        events = []
        for left, right in intervals:
            events.append((left, 1))
            events.append((right + 1, -1))

        events.sort()
        max_groups = 0
        current_groups = 0

        for _, event_type in events:
            current_groups += event_type
            max_groups = max(max_groups, current_groups)

        return max_groups
