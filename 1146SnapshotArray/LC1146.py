class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.snap_dict = defaultdict(defaultdict)
        

    def set(self, index: int, val: int) -> int:
        self.snap_dict[self.snap_id][index] =val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id -1
    

    def get(self, index: int, snap_id: int) -> int:
        curr = snap_id
        # set once, but snap many times. in this situation, we have to go to the first snap
        while curr > 0 and index not in self.snap_dict[curr]:
            curr -= 1
        if index in self.snap_dict[curr]:
            return self.snap_dict[curr][index]
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
