class MyHashSet:

    def __init__(self):
        self.mydict = {}

    def add(self, key: int) -> None:
        self.mydict[key] = True

    def remove(self, key: int) -> None:
        self.mydict.pop(key, None)

    def contains(self, key: int) -> bool:
        return key in self.mydict

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)