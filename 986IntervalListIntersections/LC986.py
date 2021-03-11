class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []
        res = []
        i =j =0
        while i < len(A) and j < len(B):
            # if overlap
            st = max(A[i][0], B[j][0])
            en = min(A[i][1], B[j][1])
            if st<= en:
                res.append([st,en])
            
            # remove smallest endpoint interval
            if A[i][1]< B[j][1]:
                i += 1
            else:
                j +=1 
        return res
                