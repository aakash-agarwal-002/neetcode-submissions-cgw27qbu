class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        prev = ""
        res = 1
        l = 0
        r = 1

        while r<len(arr):
            if arr[r-1] > arr[r] and prev != ">":
                prev = ">"
                res = max(res,r-l+1)
                r+=1
            elif arr[r-1] < arr[r] and prev != "<":
                prev = "<"
                res = max(res,r-l+1)
                r+=1
            else:
                # prev is not as expected then keep r as same
                # == then exclude == part by r+1
                r = r+1 if arr[r-1] == arr[r] else r

                # one mistake means start again 
                l = r-1
                prev = ""
        return res