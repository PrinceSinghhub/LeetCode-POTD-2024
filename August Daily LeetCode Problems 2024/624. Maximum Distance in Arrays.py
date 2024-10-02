class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_value = arrays[0][0]
        max_value = arrays[0][-1]

        max_distance = 0

        for i in range(1, len(arrays)):
            current_array = arrays[i]

            max_distance = max(max_distance, abs(current_array[-1] - min_value), abs(current_array[0] - max_value))

            if current_array[0] < min_value:
                min_value = current_array[0]
            if current_array[-1] > max_value:
                max_value = current_array[-1]

        return max_distance