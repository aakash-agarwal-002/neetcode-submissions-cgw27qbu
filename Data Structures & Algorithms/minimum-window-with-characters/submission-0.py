class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        from collections import defaultdict

        need_count = defaultdict(int)
        window = defaultdict(int)

        for c in t:
            need_count[c] += 1

        need = len(need_count)
        have = 0

        res_len = float("inf")
        res = ""

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in need_count and window[c] == need_count[c]:
                have += 1

            while have == need:
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res = s[l:r+1]

                left_char = s[l]
                window[left_char] -= 1
                if left_char in need_count and window[left_char] < need_count[left_char]:
                    have -= 1
                l += 1

        return res
