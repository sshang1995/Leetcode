class NumArray:
    #segment tree
    # 1. Preprocessing step which builds the segment tree from a given array
    # 2. Update the segment tree when an element is modified
    # 3. Calculate the Range Sum Query using the segment tree
    def __init__(self, nums: List[int]):
        if len(nums) > 0:
            self.n = len(nums)
            self.tree = [0 for _ in range(2*self.n)]
            # build segment tree
            for i in range(self.n, 2 * self.n):
                self.tree[i] = nums[i-self.n]
            for i in range(self.n-1, 0, -1):
                self.tree[i] = self.tree[i*2] + self.tree[i*2 +1]
            
    def update(self, index: int, val: int) -> None:
        index += self.n
        self.tree[index] = val
        # update segment tree
        while index > 0:
            left = right = index
            if index % 2 == 0:
                right = index +1 
            else:
                left = index -1
            # update parent (bottom-up)
            self.tree[index//2] = self.tree[left] + self.tree[right]
            index //= 2

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        sums = 0
        while left <= right:
            if left % 2 == 1:
                sums += self.tree[left]
                left += 1
            if right % 2 == 0:
                sums += self.tree[right]
                right -= 1
            # back to upper level
            left //=2
            right //=2
        return sums


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)