class Solution:
    def findClosestElements(self, arr, k, x):
        
        l = 0
        r = 0
        curr_diff = 0

        # initial window
        for i in range(k):
            curr_diff += abs(arr[i] - x)
            r += 1

        best_diff = curr_diff
        best_l = 0

        while r < len(arr):
            # slide window
            curr_diff -= abs(arr[l] - x)
            l += 1

            curr_diff += abs(arr[r] - x)
            r += 1

            if curr_diff < best_diff:
                best_diff = curr_diff
                best_l = l

        return arr[best_l:best_l + k]