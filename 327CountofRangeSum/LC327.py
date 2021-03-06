class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        first = [0]
        for num in nums:
            first.append(first[-1] + num)

        def helper(lo, hi):
            mid = (lo + hi) // 2
            if mid == lo:
                return 0
            count = helper(lo, mid) + helper(mid, hi)
            i = j = mid
            for left in first[lo:mid]:
                while i < hi and first[i] - left <  lower: i += 1
                while j < hi and first[j] - left <= upper: j += 1
                count += j - i
            first[lo:hi] = sorted(first[lo:hi])
            return count

        return helper(0, len(first))