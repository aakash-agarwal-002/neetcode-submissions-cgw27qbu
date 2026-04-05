class Solution:
    def ispalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        res = ""
        memo = {}

        def solve(i, j):
            nonlocal res

            if i > j:
                return

            if (i, j) in memo:
                return

            memo[(i, j)] = True

            # note j+1 because slicing excludes j
            if self.ispalindrome(s[i:j+1]):
                if j - i + 1 > len(res):
                    res = s[i:j+1]

            solve(i + 1, j)
            solve(i, j - 1)

        solve(0, len(s) - 1)
        return res
