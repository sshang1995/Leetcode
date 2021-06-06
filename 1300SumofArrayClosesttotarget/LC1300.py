class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        s, n = 0, len(arr)
        
        for i in range(n):
            ans = round((target - s)/n)
            if ans <= arr[i]: return ans 
            s += arr[i]
            n -= 1
            
        return arr[-1]
# TC: O(NlogN)

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr = sorted(arr, reverse = True)
        maxA = arr[0]
        while arr and arr[-1] * len(arr) < target:
            target -= arr.pop()
        return int(round((target - 0.0001) / len(arr))) if arr else maxA
            
# TC: O(NlogN)