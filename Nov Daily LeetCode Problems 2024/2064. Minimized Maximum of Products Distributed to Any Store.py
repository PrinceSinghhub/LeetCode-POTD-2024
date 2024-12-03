from typing import List

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistribute(max_products: int) -> bool:
            stores_needed = 0
            for quantity in quantities:
                stores_needed += (quantity + max_products - 1) // max_products
                if stores_needed > n:
                    return False
            return stores_needed <= n

        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid
            else:
                left = mid + 1

        return left
