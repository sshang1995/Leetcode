class Solution {
    public int scoreOfParentheses(String s) {
        Stack<Integer> stack = new Stack();
        stack.push(0);
        for (char i: s.toCharArray()){
            if (i == '('){
                stack.push(0);
            } else {
                int l = stack.pop();
                int v = stack.pop();
                stack.push(v + Math.max(2 * l, 1));
                    
            }
        }
        return stack.pop();
    }
}


class Solution {
    public int scoreOfParentheses(String s) {
        int score = 0, bal = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) =='(') {
                bal++;
            } else{
                bal--;
                if (s.charAt(i-1) == '(') {
                    score += 1 << bal;
                }
            }
            
        }
        return score;
            
    }
}