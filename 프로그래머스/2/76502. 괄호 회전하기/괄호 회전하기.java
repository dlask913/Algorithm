import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        int n = s.length();
        Deque<Character> origin = new ArrayDeque<>();
        
        // 1. 문자열 회전을 위해 Stack 으로 만들기
        for(char c : s.toCharArray()){
            origin.addLast(c);
        }
        
        for (int i=0; i<n; i++){
            Deque<Character> stack = new ArrayDeque<>();
            
            // 2. 올바른 괄호 문자열 찾기
            for (char c : origin){
                if (stack.isEmpty() && (c==')' || c=='}' || c==']')) {
                    stack.push('X');
                    break;
                }

                char str = stack.isEmpty() ? 'X' : stack.peek();
                if (c == ')' && str == '(') stack.pop();
                if (c == '}' && str == '{') stack.pop();
                if (c == ']' && str == '[') stack.pop();
                if(c == '(' || c == '{' || c == '[') stack.push(c);
            }
            
            if(stack.isEmpty()) answer ++;

            char firstChar = origin.pollFirst();
            origin.addLast(firstChar);
        }
        return answer;
    }
}