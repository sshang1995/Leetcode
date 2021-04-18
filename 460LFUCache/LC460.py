import collections
class LFUCache:
    # two dicts, one stores key and frequency, another stores frequenct and [key: value] this dict is OrderedDict using LRU logic. the first one is the least used one.
    def __init__(self, capacity: int):
        self.size = capacity
        self.keyfreq = {}
        self.minfreq = None
        self.freqkeys = collections.defaultdict(collections.OrderedDict)
        

    def get(self, key: int) -> int:
        if key not in self.keyfreq:
            return -1
        freq = self.keyfreq[key]
        val = self.freqkeys[freq][key]
        del self.freqkeys[freq][key]
        # if get(key) not put in dict yet
        if not self.freqkeys[freq]:
            if freq == self.minfreq:
                self.minfreq += 1
            del self.freqkeys[freq]
            
        self.keyfreq[key] = freq + 1
        self.freqkeys[freq+1][key] = val
        return val
        

    def put(self, key: int, value: int) -> None:
        if self.size <= 0:
            return 
        if key in self.keyfreq:
            freq = self.keyfreq[key]
            self.freqkeys[freq][key] = value
            self.get(key)
            return
        if self.size == len(self.keyfreq):
            delkey, delval = self.freqkeys[self.minfreq].popitem(last = False)
            del self.keyfreq[delkey]
        self.keyfreq[key] = 1
        self.freqkeys[1][key] = value
        self.minfreq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)