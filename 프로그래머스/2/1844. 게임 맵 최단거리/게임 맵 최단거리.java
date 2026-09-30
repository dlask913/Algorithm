import java.util.*;

class Solution {
        
    public int solution(int[][] maps) {
        int answer = -1;
        int[] dx = new int[]{1,-1,0,0};
        int[] dy = new int[]{0,0,1,-1};
        int n = maps.length;
        int m = maps[0].length;
        int[][] visited = new int[n][m];
        Deque<int[]> dq = new ArrayDeque<>();
        
        dq.offerLast(new int[]{0,0,1});
        
        while(!dq.isEmpty()){
            int[] current = dq.pollFirst();
            int x = current[0];
            int y = current[1];
            int cnt = current[2];
            
            if(x==n-1 && y==m-1) {
                answer = cnt;
                break;
            }
            
            for(int i=0; i<4; i++){
                int nx = x+dx[i];
                int ny = y+dy[i];
                
                if(0<=nx && nx<n && 0<=ny && ny<m){
                    if(maps[nx][ny] == 1 && visited[nx][ny] == 0){
                        visited[nx][ny] = 1;
                        dq.offerLast(new int[]{nx, ny, cnt+1});
                    }
                }
            }
        }
        return answer;
    }
}