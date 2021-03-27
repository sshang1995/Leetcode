class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        i , j, n = k, k, len(nums)
        res = curr_min = nums[k]
        while i > 0 or j < n-1:
            # we want always include relatively large number into the list
            if (nums[i-1] if i else 0) < (nums[j + 1] if j < n-1 else 0):
                j += 1
            else:
                i -= 1
            curr_min = min(curr_min, nums[i], nums[j])
            res = max(res, curr_min * (j -i + 1))
        return res
    