class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        m1, m2 = [0]*128, [0]*128
        need = 0
        have = 0
        minc = float('inf')
        minw = ""

        for c in t:
            m2[ord(c)] += 1

        for i in range(128):
            if m2[i] > 0:
                need += 1
        
        l = 0

        for r in range(len(s)):
            idx = ord(s[r])
            m1[idx] += 1
            if m2[idx] > 0 and m1[idx] == m2[idx]:
                have += 1

            while have == need:
                if r - l + 1 < minc:
                    minc = r - l + 1
                    minw = s[l:r+1]

                left_idx = ord(s[l])
                m1[left_idx] -= 1
                if m2[left_idx] > 0 and m1[left_idx] < m2[left_idx]:
                    have -= 1
                l += 1

        return minw
