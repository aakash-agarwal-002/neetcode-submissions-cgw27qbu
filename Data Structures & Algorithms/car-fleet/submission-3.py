class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []
        for i,j in zip(position,speed):
            cars.append((i,j))
        cars.sort(reverse=True)
        print(cars)

        for i in cars:
            if not stack:
                stack.append(i)
            else:
                p2,s2 = stack[-1]
                p1,s1 = i
                if (target-p2)/s2 < (target-p1)/s1:
                    stack.append(i)
        
        return len(stack)



