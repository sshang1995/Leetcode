class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(l, m, r):
            a, b = nums[l:m+1], nums[m+1:r+1]
            for i in range(l, r + 1)[::-1]:
                if not b or a and a[-1] > b[-1]:
                    nums[i] = a.pop()
                else:
                    nums[i] = b.pop()
       
        def ms(l, r):
            if l >= r: return 0
            mid = (l + r) // 2
            # recursive call
            count = ms(l, mid) + ms(mid + 1, r)

            j = mid + 1
            for i in range(l, mid+1):
                while j <= r and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - mid - 1

            #nums[l:r+1] = sorted(nums[l:r+1])
            merge(l, mid, r)
            return count

        return ms(0, len(nums) - 1)