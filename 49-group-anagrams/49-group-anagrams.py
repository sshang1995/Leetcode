  
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = defaultdict(list)
        for word in strs:
            
            dicts[tuple(sorted(word))].append(word)
        return dicts.values()