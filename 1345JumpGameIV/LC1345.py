class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <=1:
            return 0
        dicts = defaultdict(list)
        for i in range(n):
            dicts[arr[i]].append(i)
        q = [0]
        visited = set()
        steps  = 0
        while q:
            nex = []
            for node in q:
                if node == n-1:
                    return steps
                for child in dicts[arr[node]]:
                    visited.add(child)
                    nex.append(child)
                dicts[arr[node]].clear()
                for i in [node-1, node+1]:
                    if 0 <= i< n and i not in visited:
                        visited.add(i)
                        nex.append(i)
            q = nex
            steps +=1
        return -1
# BFS with memo
# TC: O(N)
# SC: O(N)