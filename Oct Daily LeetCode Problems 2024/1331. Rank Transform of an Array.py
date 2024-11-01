class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []

        # Step 1: Create a sorted list of unique elements
        unique_sorted = sorted(set(arr))

        # Step 2: Create a rank mapping
        rank_map = {num: rank + 1 for rank, num in enumerate(unique_sorted)}

        # Step 3: Replace elements in the original array with their ranks
        return [rank_map[num] for num in arr]
