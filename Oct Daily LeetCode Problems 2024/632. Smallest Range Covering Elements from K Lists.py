from heapq import heappush, heappop
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Initialize the heap and current max
        minHip = []
        maxNum = float('-inf')

        # Push the first element of each list into the heap
        for i in range(len(nums)):
            # (value, list_index, element_index)
            heappush(minHip, (nums[i][0], i, 0))
            maxNum = max(maxNum, nums[i][0])

        print(minHip)
        ansRange = [-float('inf'), float('inf')]

        # Process the heap
        while minHip:
            data, listImdx, dataIndx = heappop(minHip)

            # Update the range if the current one is smaller
            if maxNum - data < ansRange[1] - ansRange[0]:
                ansRange = [data, maxNum]

            # If the list is exhausted, break
            if dataIndx + 1 == len(nums[listImdx]):
                break

            # Push the next element from the same list into the heap
            tempData = nums[listImdx][dataIndx + 1]
            heappush(minHip, (tempData, listImdx, dataIndx + 1))
            maxNum = max(maxNum, tempData)

        return ansRange
