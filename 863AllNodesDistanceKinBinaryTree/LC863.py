class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        dicts = defaultdict(list)
        visited = set()
        res = []
        # for each node as key, save it's left, right, parent
        def dfs(node):
            if node.left:
                dicts[node].append(node.left)
                dicts[node.left].append(node)
                dfs(node.left)
            if node.right:
                dicts[node].append(node.right)
                dicts[node.right].append(node)
                dfs(node.right)
        dfs(root)
        # start from target, find distance k nodes.ConnectionAbortedError
        def bfs(node, d):
            if d < K:
                visited.add(node)
                for v in dicts[node]:
                    if v not in visited:
                        bfs(v, d+1)
            else:
                res.append(node.val)
        bfs(target, 0)
        return res

# TC: O(N)
#SC: O (N)

# Solution 2
class Solution(object):
    def distanceK(self, root, target, K):
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d+1))

        return []
# Solution 3:
class Solution(object):
    def distanceK(self, root, target, K):
        ans = []

        # Return distance from node to target if exists, else -1
        # Vertex distance: the # of vertices on the path from node to target
        def dfs(node):
            if not node:
                return -1
            elif node is target:
                subtree_add(node, 0)
                return 1
            else:
                L, R = dfs(node.left), dfs(node.right)
                if L != -1:
                    if L == K: ans.append(node.val)
                    subtree_add(node.right, L + 1)
                    return L + 1
                elif R != -1:
                    if R == K: ans.append(node.val)
                    subtree_add(node.left, R + 1)
                    return R + 1
                else:
                    return -1

        # Add all nodes 'K - dist' from the node to answer.
        def subtree_add(node, dist):
            if not node:
                return
            elif dist == K:
                ans.append(node.val)
            else:
                subtree_add(node.left, dist + 1)
                subtree_add(node.right, dist + 1)

        dfs(root)
        return ans
