class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order_dict = {c:i for i,c in enumerate(order)}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if order_dict[w1[j]] < order_dict[w2[j]]:
                    break
                elif order_dict[w1[j]] > order_dict[w2[j]]:
                    return False
        return True