public class Solution {
    public int[][] IntervalIntersection(int[][] A, int[][] B) {
        if (A is null){
            return A;
        }
        if (B is null){
            return B;
        }
        
        List<int[]> res = new List<int[]>();
        int i =0; 
        int j =0;
        while (i < A.Length && j < B.Length){
            int st = Math.Max(A[i][0], B[j][0]);
            int en = Math.Min(A[i][1], B[j][1]);
            if (st <= en){
                res.Add(new int[]{st,en});
            }
            
            if(A[i][1] < B[j][1]){
                i++;
            }
            else{
                j++;
            }
        }
        return res.ToArray();
        
        
    }
}