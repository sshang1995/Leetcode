from collections import defaultdict
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in nums1:
            d1[i*i] += 1
        for i in nums2:
            d2[i*i] += 1
        res = 0   
        for i in range(len(nums1)-1):
            for j in range(i+1, len(nums1)):
                curr = nums1[i]* nums1[j]
                if curr in d2:
                    res += d2[curr]
        
        for i in range(len(nums2)-1):
            for j in range(i+1, len(nums2)):
                curr = nums2[i]* nums2[j]
                if curr in d1:
                    res += d1[curr]           
        return res     
#TC: O(N^2*M + M^2*N)
#SC: O(N+M)         