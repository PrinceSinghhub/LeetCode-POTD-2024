class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        # initialize the number of boats with zero
        boat = 0

        # initialize the left and the right pointers
        right = len(people) - 1
        left = 0

        while right >= left:
            # if the weight of current smallest and the current largest is greater tha the                 limit then include only the larger weight
            if people[right] + people[left] > limit:
                boat += 1
                right -= 1

            # Else include both people and shith both the pointers
            else:
                boat += 1
                right -= 1
                left += 1

        # return the total number of boats
        return boat
