class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        res = []
        for i in nums:
            map[i] = map.get(i,0) + 1
        mydict = dict(sorted(map.items(), key=lambda item: item[1],reverse=True))
        print(mydict)
        for i,key in enumerate(mydict.keys()):
            if i==k:
                break
            res.append(key)
        return res

