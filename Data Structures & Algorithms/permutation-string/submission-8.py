class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
            
        map1 = [0]*26
        map2 = [0]*26
        matches = 0

        for i in range(len(s1)):
            map1[ord(s1[i]) - ord('a')] += 1
            map2[ord(s2[i]) - ord('a')] += 1
        
        l = 0
        r = len(s1) - 1

        for i in range(26):
            if map1[i] == map2[i]:
                matches += 1
        
        while r < len(s2):
            if matches == 26:
                return True

            idx = ord(s2[l]) - ord('a')
            if map2[idx] == map1[idx]:
                matches -= 1
            map2[idx] -= 1
            if map2[idx] == map1[idx]:
                matches += 1

            l += 1
            r += 1
            if r == len(s2):
                break

            idx = ord(s2[r]) - ord('a')
            if map2[idx] == map1[idx]:
                matches -= 1
            map2[idx] += 1
            if map2[idx] == map1[idx]:
                matches += 1
            
        return False
