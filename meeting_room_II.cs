public class Solution {
    public int MinMeetingRooms(int[][] intervals) {
        int[] st = new int[intervals.Length];
        int[] en = new int[intervals.Length];
        
        int num = 0;
        foreach(int[] interval in intervals){
            st[num]= interval[0];
            en[num] = interval[1];
            num++;
        }
        
        Array.Sort(st);
        Array.Sort(en);
        int rooms = 0;
        int i =0;
        int j = 0;
        while(i < intervals.Length){
            if (st[i]>=en[j]){
                rooms--;
                j+=1;    
            }
            rooms++;
            i+=1;
        }
        return rooms;
        
        
            
    }
}