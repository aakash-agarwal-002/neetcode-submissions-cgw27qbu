class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        for i in range(len(hand)//groupSize):
            mine = min(hand)
            print(mine)
            for j in range(groupSize):
                if mine not in hand:
                    return False
                hand.remove(mine)
                mine+=1

        return True
