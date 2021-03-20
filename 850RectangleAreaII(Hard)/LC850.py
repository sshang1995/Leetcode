# line sweep
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # line sweep (from bottom to top)
        open = 1
        close = 0
        events = []
        #scan all rectangles.
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, open, x1, x2))
            events.append((y2, close, x1, x2))
        # sort based on y
        events.sort()
        
        def query():
            ans = 0
            cur = -1
            for x1, x2 in active:
                cur = max(cur , x1)
                # get current wide
                ans += max(0, x2 - cur)
                cur = max(cur, x2)
            return ans
        
        active = []
        cur_y = events[0][0]
        ans = 0
        for y, typ, x1, x2 in events:
            
            # for all vertical ground covered, update answer
            # calculate area 
            ans += query() * (y - cur_y)
            
            # Update active 
            if typ is open:
                active.append((x1,x2))
                active.sort()
            else:
                active.remove((x1,x2))
                
            cur_y = y 
            
        return ans % (10**9 + 7)
    
#TC: O(N^2logN)  
#SC: O(N)

# seg
        