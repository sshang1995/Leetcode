class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # get the smallest right end.
        j = len(arr) - 1
        while j and arr[j-1] <= arr[j]:
            j -= 1
        
        #start from 0 to j [0,j), find the largest left point
        i = 0
        res = j - i
        if res == 0:
            return res
        # j += 1, find any possible interval.
        while j <= len(arr):
            # sliding window, [i,j)
            while (i== 0 or arr[i-1]<= arr[i]) and (j == len(arr) or arr[i] <= arr[j]):
                i+=1
                res = min(res, j-i)
                if res == 0:
                    return 0
                
            j += 1
        return res