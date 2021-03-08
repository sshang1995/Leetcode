class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        st = []
        en = []
        for i in intervals:
            st.append(i[0])
            en.append(i[1])
        st= sorted(st)
        en = sorted(en)
        
        i,j = 0,0
        room = 0
        while i < len(intervals):
            # For every interval, add room once, but if st[i] > en[j], that means we can 
            #resue the room, so room -1.
            if st[i] >= en[j]:
                room -= 1
                j +=1
            room +=1
            i+=1
        return room