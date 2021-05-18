class Solution {
    public boolean checkValidString(String s) {
        int c_min = 0, c_max = 0;
        for (char i: s.toCharArray()) {
            if (i == '(') {
                c_min++;
                c_max++;      
            }else if (i == ')') {
                c_max--;
                c_min = Math.max(--c_min, 0);
            }else {
                c_max++;
                c_min = Math.max(--c_min, 0); 
            }
            if (c_max < 0) {
                return false;
            }
        }
        return c_min == 0;
            
    }
}