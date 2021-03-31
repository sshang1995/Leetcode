class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        l = max(weights)
        r = sum(weights)
        while l < r:
            count = 1
            sums = 0
            mid = (l + r) //2
            for w in weights:
                if sums + w > mid:
                    count += 1
                    sums = 0
                sums += w
            #print(f"l:{l},mid:{mid},r:{r},d:{count}")
            if count <= D:
                r = mid
            else:
                l = mid + 1

        return l
    