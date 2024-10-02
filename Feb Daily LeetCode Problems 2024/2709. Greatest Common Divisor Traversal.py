class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums)<=1: return True
        if 1 in nums:
            return False
        p = dict()
        def find(x):
            if x not in p:
                p[x] = x
            if p[x]==x:
                return  x
            p[x] = find(p[x])
            return p[x]
        s = set(nums)
        ma = max(nums)
        sieve = [False]*(ma)
        sieve[0]=True
        i = 2
        while i<=ma:
            if sieve[i-1]==True:
                i+=1
                continue

            mi = i
            for j in range(ma//i+1):
                if j*i<=ma:
                    sieve[j*i-1] = True
                    if j*i in s:
                        if find(j*i)==j*i:
                            continue
                        else:
                            mi = p[j*i]
            for j in range(ma//i+1):
                if j*i in s:
                    p[find(j*i)] = mi
            i+=1
        # print(p)
        t = find(nums[0])
        for i in s:
            if find(i)!=t:
                return False
        return True
        # return all(p[i] for i in nums)