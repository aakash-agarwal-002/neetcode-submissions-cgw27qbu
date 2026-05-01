class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        side = sum(matchsticks)//4

        if len(matchsticks)<4:
            return False

        if sum(matchsticks)%4 != 0:
            return False

        sides = [0]*4
        matchsticks.sort(reverse=True)
        
        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if matchsticks[i] + sides[j] <= side:
                    sides[j]+=matchsticks[i] 
                    if backtrack(i+1):
                        return True
                    sides[j]-=matchsticks[i] 

            return False
        return backtrack(0)
