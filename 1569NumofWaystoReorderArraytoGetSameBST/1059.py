import math
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        #math.comb(n, k)
        # get number of ways to choose k items from n items.
        # without repetitiona adn without order
        def helper(nums):
            if len(nums) <=2:
                return 1
            left = [v for v in nums if v < nums[0]]
            right = [v for v in nums if v > nums[0]]
            return math.comb(len(left)+len(right), len(right)) * helper(left)*helper(right)
        # helper(left) arranged_ways_in_left, vice versa
        return (helper(nums)-1) % (10**9+7)
        # -1 means remove the  result one

        