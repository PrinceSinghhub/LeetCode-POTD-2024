from collections import Counter
class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        unique_cards = sorted(count.keys())

        for card in unique_cards:
            while count[card] > 0:
                for i in range(card, card + groupSize):
                    if count[i] <= 0:
                        return False
                    count[i] -= 1

        return True