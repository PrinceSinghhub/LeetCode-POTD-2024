class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i in range(1, len(rating)-1):
            smallerLeft = 0
            smallerRight = 0
            biggerLeft = 0
            biggerRight = 0
            middle = rating[i]
            for j in range(i):
                if(rating[j] < middle):
                    smallerLeft += 1
                else:
                    biggerLeft += 1
            for j in range(i+1, len(rating)):
                if(rating[j] < middle):
                    smallerRight += 1
                else:
                    biggerRight += 1
            count += smallerLeft * biggerRight
            count += biggerLeft * smallerRight
        return count

