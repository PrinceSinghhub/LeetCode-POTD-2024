class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        freq = list(freq.values())
        last_row = freq.count(max_freq)
        ans = (max_freq - 1) * (n + 1) + last_row
        return max(len(tasks), ans)
