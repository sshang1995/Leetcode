class Solution {
    public String minRemoveToMakeValid(String s) {
        Stack<Integer> open = new Stack<Integer>();
        Set<Integer> close = new HashSet<>();
        for (int i = 0; i< s.length(); i++) {
            if (s.charAt(i) == '(') {
                open.push(i);
            } else if (s.charAt(i) == ')') {
                if (open.isEmpty()) {
                    close.add(i);
                }else {
                    open.pop();}
            } 
        }
        while (!open.isEmpty()) close.add(open.pop());
        
        StringBuilder str = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (!close.contains(i)) {
                str.append(s.charAt(i));
            }
        }
        return str.toString();
        
    }
}