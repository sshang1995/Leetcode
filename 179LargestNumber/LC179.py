# bubble sort
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(n1, n2):
            return str(n1) + str(n2) > str(n2) + str(n1)
        for i in range(len(nums),0,-1):
            for j in range(i-1):
                if not compare(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return str(int("".join(map(str,nums))))
# TC: O(N ^2)
# SC: O(1)


# merge Sort
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(n1, n2):
            return str(n1) + str(n2) > str(n2) + str(n1)
        
        def mergeSort(nums, l, r):
            if l == r:
                return [nums[l]]
            if l > r:
                return 
            mid = (l+r)//2
            left = mergeSort(nums, l, mid)
            right = mergeSort(nums, mid+1, r)
            return merge(left, right)
        def merge(left, right):
            l , r = 0, 0
            res = []
            while l < len(left) and r < len(right):
                if compare(left[l], right[r]):
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
            res.extend(left[l:] or right[r:])
            return res
        nums = mergeSort(nums, 0, len(nums)-1)
        return str(int("".join(map(str, nums))))
# TC: O(NlogN)  
# SC: O(N)    

# built-in 
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest = ''.join(sorted(map(str, nums), key = LargeNum))
        return  '0' if largest[0] == '0' else largest
       
class LargeNum(str):
    def __lt__(a, b):
        return a + b > b + a

# TC: O(NlogN)
# SC: O(N) 
    
        
       
                
                
                