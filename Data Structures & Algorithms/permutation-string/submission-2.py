class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
            
        map1 = dict()
        map2 = dict()

        for i in range(len(s1)):
            map1[s1[i]] = map1.get(s1[i], 0) + 1

        j = 0
        while j < len(s1):
            map2[s2[j]] = map2.get(s2[j], 0) + 1
            j += 1

        l = 0
        r = j - 1

        while r < len(s2):
            if map1 == map2:
                return True
            else:
                map2[s2[l]] -= 1
                if map2[s2[l]] == 0:
                    del map2[s2[l]]
                l += 1

                r += 1
                if r < len(s2):
                    map2[s2[r]] = map2.get(s2[r], 0) + 1

        return False
