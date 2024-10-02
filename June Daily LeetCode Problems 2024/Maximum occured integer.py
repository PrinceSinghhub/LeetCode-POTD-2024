# User function Template for python3

class Solution:
    # Function to find the maximum occurred integer in all ranges.
    def maxOccured(self, n, l, r, maxx):
        arr = [0] * (maxx + 2)

        # Increment start points and decrement end points
        for i in range(n):
            arr[l[i]] += 1
            arr[r[i] + 1] -= 1

        # Finding the maximum occurred integer
        occur = 0
        ansindx = 0
        maxoccur = 0

        for i in range(maxx + 1):
            occur += arr[i]
            if occur > maxoccur:
                maxoccur = occur
                ansindx = i

        return ansindx


# {
# Driver Code Starts
# Initial Template for Python 3

import math

A = [0] * 1000000


def main():
    T = int(input())

    while (T > 0):
        global A
        A = [0] * 1000000

        n = int(input())

        l = [int(x) for x in input().strip().split()]
        r = [int(x) for x in input().strip().split()]

        maxx = max(r)
        ob = Solution()
        print(ob.maxOccured(n, l, r, maxx))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends