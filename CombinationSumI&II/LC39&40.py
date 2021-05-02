# 39
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(remain, comb, start):
            if remain == 0:
                res.append(list(comb))
                return 
            elif remain < 0:
                return
        
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                dfs(remain-candidates[i], comb, i)
                comb.pop()
        dfs(target, [],0)
        return res
# 40, each value only use once
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(remain, index, comb, counter):
            if remain == 0:
                res.append(list(comb))
                return
            elif remain < 0:
                return
        
            for i in range(index, len(counter)):
                candidate, freq = counter[i]
                if freq <= 0:
                    continue
                
                comb.append(candidate)
                counter[i] = (candidate, freq -1)
                dfs(remain-candidate, i, comb, counter)
                
                counter[i] = (candidate, freq)
                comb.pop()
        counter = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]
        
        dfs(target, 0, [], counter)
        return res

                
