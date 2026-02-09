class FrequencyTracker:

    def __init__(self):
        self.mapp=defaultdict(int)
        self.cmapp=defaultdict(int)

    def add(self, number: int) -> None:
        old=self.mapp[number]
        new=self.mapp[number]+1
        self.mapp[number]=new
        if old>0:
            self.cmapp[old]-=1
        self.cmapp[new]+=1

    def deleteOne(self, number: int) -> None:
        if self.mapp[number]>0:
            old=self.mapp[number]
            new=old-1
            self.mapp[number]=new
            self.cmapp[old]-=1

            if new>0:
                self.cmapp[new]+=1
            else:
                del self.mapp[number]
            
    def hasFrequency(self, frequency: int) -> bool:
        return self.cmapp[frequency]>0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
