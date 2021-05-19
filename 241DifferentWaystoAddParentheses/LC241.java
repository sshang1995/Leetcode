class Solution {
    Map<String,List<Integer>> memo = new HashMap<>();
    public List<Integer> diffWaysToCompute(String expression) {
        List<Integer> res = new ArrayList<>();
        if (memo.containsKey(expression)) {
                return memo.get(expression);
        }
        
        if (!containOperator(expression)){
            res.add(Integer.parseInt(expression));
            return res;
        }
        
        for (int i = 0; i < expression.length(); i++) {
            char ch = expression.charAt(i);
            if (ch == '+' || ch == '-' || ch == '*') {
                List<Integer> left = diffWaysToCompute(expression.substring(0,i));
                List<Integer> right = diffWaysToCompute(expression.substring(i+1));
                for (int l: left){
                    for (int r: right) {
                        switch(ch) {
                            case '+':
                                res.add(l+r);
                                break;
                            case '-':
                                res.add(l-r);
                                break;
                            default: //*
                                res.add(l*r);
                            
                        }
                    }
                }
                memo.put(expression, res);
                
            }
            
        }
        //memo.put(expression, res);
        return res;
     
    }
    
    
    public boolean containOperator(String expression) {
        if (expression.length() == 0){
            return false;
        } 
        for(char i: expression.toCharArray()) {
            if(i == '+'|| i=='-' || i == '*') {
                return true;
            }
        
        }
        return false;   
    }
    
    
}