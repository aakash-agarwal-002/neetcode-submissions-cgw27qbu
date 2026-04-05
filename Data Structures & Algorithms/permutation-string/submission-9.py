class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        for i in range(n):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1

        if freq1 == freq2:
            return True

        for i in range(n, m):
            freq2[ord(s2[i]) - ord('a')] += 1
            freq2[ord(s2[i - n]) - ord('a')] -= 1

            if freq1 == freq2:
                return True

        return False
