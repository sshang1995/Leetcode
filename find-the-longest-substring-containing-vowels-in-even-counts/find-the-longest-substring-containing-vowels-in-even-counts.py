class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        lists = [(False, False, False, False, False)]
        vowels = {
            'a': 0,
            'e': 1,
            'i': 2,
            'o': 3,
            'u': 4
        }
        for char in s:
            prev = list(lists[-1])
            if char in vowels:
                prev[vowels[char]]= not prev[vowels[char]] #"False to True, or True to False, even number of vowel will be false"
            lists.append(tuple(prev))

        seen = {}
        res = 0
        for i, v in enumerate(lists):
                if v in seen:
                    res = max(res, i-seen[v])
                else:
                    seen[v] = i
        return res