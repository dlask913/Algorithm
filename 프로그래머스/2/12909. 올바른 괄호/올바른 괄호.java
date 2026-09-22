import java.util.*;
class Solution {
    boolean solution(String s) {
        boolean answer = true;
        ArrayDeque<Character> stack = new ArrayDeque<>();
        int n = s.length();

        for(int i=0; i<n; i++){
            Character tmp = s.charAt(i);
            if(tmp == ')'){
                if(stack.isEmpty() || stack.peek()==')') return false;
                stack.pop();
            } else {
                stack.push('(');
            }
        }
        
        if(!stack.isEmpty()) return false;
        
        return answer;
    }
}