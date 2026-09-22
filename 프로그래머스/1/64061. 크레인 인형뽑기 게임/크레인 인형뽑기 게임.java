import java.util.*;
class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int n = board.length;
        int[] idx = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        
        
        // 1. 열마다 가장 상단의 인형 위치 저장
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(board[j][i] > 0){
                    idx[i] = j;
                    break;
                }
            }
        }
        
        // 2. 인형 뽑기
        for (int x : moves){
            int doll = board[idx[x-1]][x-1];
            if(doll == 0) continue;
            
            if(!stack.isEmpty() && stack.peek() == doll) {
                answer += 2;
                stack.pop();
            }
            else stack.push(doll);
            
            // 인형 위치 갱신
            board[idx[x-1]][x-1] = 0;
            if (idx[x-1]+1 < n) idx[x-1] ++;
        }
        
        return answer;
    }
}