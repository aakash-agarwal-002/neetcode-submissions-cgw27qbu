class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair  = [[p,s] for p,s in zip(position,speed)]
        pair.sort()
        stack = []

        for i in range(len(pair)-1,-1,-1):
            time = (target-pair[i][0])/pair[i][1]
            stack.append(time)
            if len(stack) >=2 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)