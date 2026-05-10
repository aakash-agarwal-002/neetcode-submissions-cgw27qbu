class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_dict = Counter(t)
        for i in s:
            t_dict[i]-=1

        print(t_dict)
        for i,j in t_dict.items():
            if j == 1:
                return i
        return ""