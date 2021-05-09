class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        
        n = len(A)
        next_min_higher, next_max_lower = [0] * n, [0] * n

        stack = []
        # sort from small to large
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_min_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        # sort from large to small
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_max_lower[stack.pop()] = i
            stack.append(i)

        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1
        for i in range(n - 1)[::-1]:
            higher[i] = lower[next_min_higher[i]]
            lower[i] = higher[next_max_lower[i]]
        return sum(higher)
# TC: O(NlogN)
# SC: O(N)

# We need to jump higher and lower alternately to the end.

# Take [5,1,3,4,2] as example.

# If we start at 2,
# we can jump either higher first or lower first to the end,
# because we are already at the end.
# higher(2) = true
# lower(2) = true

# If we start at 4,
# we can't jump higher, higher(4) = false
# we can jump lower to 2, lower(4) = higher(2) = true

# If we start at 3,
# we can jump higher to 4, higher(3) = lower(4) = true
# we can jump lower to 2, lower(3) = higher(2) = true

# If we start at 1,
# we can jump higher to 2, higher(1) = lower(2) = true
# we can't jump lower, lower(1) = false

# If we start at 5,
# we can't jump higher, higher(5) = false
# we can jump lower to 4, lower(5) = higher(4) = false

