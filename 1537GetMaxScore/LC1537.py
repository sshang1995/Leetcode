class Solution:
	def maxsum(self, A: List[int], B:List[int]) -> int:
		# Two pointers
		i, j, n, m = 0, 0, len(A), len(B)
		a , b , mod = 0, 0, 10 ** 9 + 7
		while i < n or j < m:
			if i < n and (j == m or A[i] < B[j]):
				a += A[i]
				i += 1
			elif j < m and (i == n or A[i] > B[j]):
				b += B[j]
				j += 1
			else: # when A[i] = B[j], checkpoint
				a = b = max(a,b) + A[i] # reset sum, add max path into sum
				i += 1
				j += 1
		return max(a,b)% mod

class Solution:
    def maxSum(self, A: List[int], B: List[int]) -> int:
        # Two pointers, 
        # Max score = Max prefixsum(a,b)  + checkpoint + max postfixsum (a,b)
        i, j, n, m = 0, 0, len(A), len(B)
        a , b , mod = 0, 0, 10 ** 9 + 7
        res = 0
        while i < n and j < m:
            if A[i] < B[j]:
                a += A[i]
                i += 1
            elif A[i] > B[j]:
                b += B[j]
                j += 1
            else:
                res += max(a,b) + A[i]
                i += 1
                j += 1
                a = 0
                b = 0
        while i < n:
            a += A[i]
            i +=1
        while j < m:
            b += B[j]
            j += 1
        return (res + max(a,b)) % mod