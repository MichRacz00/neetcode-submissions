class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        freqs = {}

        for card in hand:
            freqs[card] = 1 + freqs.get(card, 0)
        
        i = 0
        while freqs:
            currCard = min(freqs)
            for i in range(groupSize):
                if currCard not in freqs:
                    return False
                freqs[currCard] -= 1
                if freqs[currCard] == 0:
                    del freqs[currCard]
                currCard += 1
        
        return True