class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        for i in nums:
            mydict[i] = mydict.get(i, 0) + 1

        mydict = sorted(mydict.items(),key=lambda x:x[1],reverse=True)
        print(mydict)
        return [key for i,(key,_) in enumerate(mydict) if i<k]