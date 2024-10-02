import heapq


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        freq_map = {}
        for num in arr:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        min_heap = [(freq, num) for num, freq in freq_map.items()]
        heapq.heapify(min_heap)

        while k > 0:
            freq, num = heapq.heappop(min_heap)
            if k >= freq:
                k -= freq
            else:
                freq -= k
                k = 0
                heapq.heappush(min_heap, (freq, num))

        return len(min_heap)