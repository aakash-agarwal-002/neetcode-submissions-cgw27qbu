class MyHashSet:

    def __init__(self):
        self.mydict = dict()

    def add(self, key: int) -> None:
        if key not in self.mydict.keys():
            self.mydict[key] = ""

    def remove(self, key: int) -> None:
        if key in self.mydict.keys():
            self.mydict.pop(key)
        

    def contains(self, key: int) -> bool:
        if key in self.mydict.keys():
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)