import java.util.*;

class Solution {
    public String solution(int n, int k, String[] cmd) {
        int[] up = new int[n+2];
        int[] down = new int[n+2];
        Deque<Integer> deleted = new ArrayDeque<>();
        
        // 1. 각 k에 대한 위 아래 위치 저장
        for(int i=0; i<n+2; i++){
            up[i] = i-1;
            down[i] = i+1;
        }
        
        // 앞뒤 더미 배치를 위해 1-based index 로 변경
        k++;
        
        // 2. 커맨드 수행
        for(String s: cmd){
            String[] parts = s.split(" ");
            if(parts[0].equals("C")){ // 삭제
                deleted.push(k);
                up[down[k]] = up[k];
                down[up[k]] = down[k];
                if(down[k] <= n) k = down[k];
                else k = up[k];
            } else if(parts[0].equals("Z")){ // 되돌리기
                int restored = deleted.pop();
                down[up[restored]] = restored;
                up[down[restored]] = restored;
            } else if(parts[0].equals("U")){ // 위로 
                int dx = Integer.parseInt(parts[1]);
                for(int i=0; i<dx; i++){
                    k = up[k];
                }            
            } else if(parts[0].equals("D")){ // 아래로
                int dx = Integer.parseInt(parts[1]);
                for(int i=0; i<dx; i++){
                    k = down[k];
                }
            }
        }
        
        // 3. 삭제되지 않은 행은 O, 삭제된 행은 X 
        char[] answer = new char[n];
        Arrays.fill(answer, 'O');
        for(int i: deleted){
            answer[i-1] = 'X';
        }

        return new String(answer);
    }
}