class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        
        head = mat[0][:]
        for row in mat[1:]:
            ls = []
            for j in head:
                for i in row:
                    ls.append(j + i)
            head = sorted(ls)[:k]
        return head[k-1]
    
#         h = mat[0][:]
#         for row in mat[1:]:
#             h = sorted([i+j for i in row for j in h])[:k]
#             print(h)
#         return h[k-1]
        