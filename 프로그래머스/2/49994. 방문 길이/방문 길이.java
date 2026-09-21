import java.util.*;

class Solution {
    public int solution(String dirs) {
        Set<String> visited = new HashSet<>();
        int n = dirs.length();
        int x = 0;
        int y = 0;
        int[] dx = {-1,1,0,0}; // L, R, U, D
        int[] dy = {0,0,1,-1};
        
        for(int i=0; i<n; i++){
            int tx = x;
            int ty = y;
            if(dirs.charAt(i) == 'L'){
                tx += dx[0];
                ty += dy[0];
            } else if(dirs.charAt(i) == 'R'){
                tx += dx[1];
                ty += dy[1];
            } else if(dirs.charAt(i) == 'U'){
                tx += dx[2];
                ty += dy[2];
            } else if(dirs.charAt(i) == 'D'){
                tx += dx[3];
                ty += dy[3];
            }
            if (Math.abs(tx) > 5 || Math.abs(ty) > 5) continue;
            // 이전 좌표랑 현 좌표 둘 다 저장, 순서 바뀐 경우 예외
            if (!visited.contains(tx+","+ty+","+x+","+y)){
                visited.add(x+","+y+","+tx+","+ty); 
            }
            x = tx; 
            y = ty;
        }
        
        return visited.size();
    }
}