class AllOne:

    def __init__(self):
        self.dic = {}
        self.res = ""

    def inc(self, key: str) -> None:
        if key in self.dic:
            self.dic[key] += 1
        else:
            self.dic[key] = 1
        return None

    def dec(self, key: str) -> None:
        if self.dic[key] > 1:
            self.dic[key] -= 1
        else:
            self.dic.pop(key)
        return None

    def getMaxKey(self) -> str:
        if not self.dic:
            return ""
        return max(self.dic, key=self.dic.get)

    def getMinKey(self) -> str:
        if not self.dic:
            return ""
        return min(self.dic, key=self.dic.get)

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()