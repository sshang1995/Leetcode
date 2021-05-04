class Solution:
    def jump(self, nums: List[int]) -> int:
        # greegy
        jumps, current_end, farthest = 0,0,0
        for i in range(len(nums)-1):
            #for every index, save the furthest position
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps