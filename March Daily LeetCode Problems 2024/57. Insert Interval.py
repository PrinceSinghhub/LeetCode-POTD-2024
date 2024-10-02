class Solution:
    def insert(self, intervel: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervel.append(newInterval)

        if len(intervel) == 0:
            return intervel

        intervel.sort()

        merged = []

        start = intervel[0][0]
        end = intervel[0][1]

        for i in intervel:
            if i[0] <= end:
                end = max(end, i[1])
            else:
                merged.append([start, end])
                start = i[0]
                end = i[1]

        merged.append([start, end])

        return merged



