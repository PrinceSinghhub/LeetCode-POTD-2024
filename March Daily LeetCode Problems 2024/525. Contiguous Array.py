class Solution:
    def findMaxLength(self, nums):

        mydic = {}
        mydic[0] = -1

        sum = 0
        current = 0
        for key,value in enumerate(nums):
            if value == 1:
                current+=1
            else:
                current-=1

            if current in mydic:
                sum = max(sum,key-mydic[current])
            else:
                mydic[current] = key
        print(mydic)
        return sum