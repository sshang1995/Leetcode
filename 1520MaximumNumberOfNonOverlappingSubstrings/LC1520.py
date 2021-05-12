class Solution:
    def maxNumOfSubstrings(self, s):
        fst = { c : i for i, c in reversed(list(enumerate(s))) }
        lst = { c : i for i, c in enumerate(s) }
        
        intervals = []
        for c in set(s):
            b, e = fst[c], lst[c]
            i = b
            while i <= e and b == fst[c]:
                b = min(b, fst[s[i]])
                e = max(e, lst[s[i]])
                i += 1
            if b == fst[c]:
                intervals.append((e, b))
        
        intervals.sort()
        ans, prev = [], -1
        for e, b in intervals:
            if b > prev:
                ans.append(s[b:e + 1])
                prev = e
        
        return ans
# TC: O(N*26)
# SC: O(N)

class Solution:
    def maxNumOfSubstrings(self, s):
        fst = { c : i for i, c in reversed(list(enumerate(s))) }
        lst = { c : i for i, c in enumerate(s) }
        # max number is 26 character, making sure evry string has unique char
        ans, prev = [], -1
        for i in sorted(lst.values()): # start from earliest end 
            b, e = fst[s[i]], lst[s[i]]
            j = e
            while j >= b and b > prev and e == i: #abab: aba is not qualify
                b = min(b, fst[s[j]])
                e = max(e, lst[s[j]])
                j -= 1
            # only append substring after prev end
            if b > prev and e == i:
                ans.append(s[b:e + 1])
                prev = e
        
        return ans