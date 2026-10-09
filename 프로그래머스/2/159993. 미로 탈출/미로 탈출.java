import java.util.*;

/* S : 시작 지점, E : 출구, L : 레버, O : 통로, X : 벽 */
// 1. 시작 지점~ 레버까지 최소 비용 ( S -> L )
// 2. 레버 ~ 출구까지 최소 비용 ( L -> E)
// 3. 각 최소 비용 더하기
class Node {
    int x,y,cost;
    
    Node(int x, int y, int cost){
        this.x = x;
        this.y = y;
        this.cost = cost;
    }
}

class Solution {
    int[] dx = new int[]{1, -1, 0, 0};
    int[] dy = new int[]{0, 0, 1, -1};
    public int solution(String[] maps) {
        int toLever = escapeSpace(maps, 'S', 'L');
        int toEnd = escapeSpace(maps, 'L', 'E');
        
        if(toLever == -1 || toEnd == -1) return -1;

        return toLever + toEnd;
    }
    
    int escapeSpace(String[] maps, char start, char end){
        int n = maps.length;
        int m = maps[0].length();
        int[][] visited = new int[n][m];
        Deque<Node> dq = new ArrayDeque<>();
        // 시작점 좌표 구하기
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(maps[i].charAt(j) == start){
                    dq.offer(new Node(i,j,0));
                    break;
                }
            }
        }
        
        // 출발 ~ 도착까지 최소 비용 구하기
        while(!dq.isEmpty()){
            Node cur = dq.poll();
            if(visited[cur.x][cur.y] == 1) continue;
            visited[cur.x][cur.y] = 1;
            if(maps[cur.x].charAt(cur.y) == end) {
                return cur.cost;
            }
            
            for(int i=0; i<4; i++){
                int nx = dx[i] + cur.x;
                int ny = dy[i] + cur.y;
                if(0<=nx && nx<n && 0<=ny && ny<m){
                    if(visited[nx][ny] == 0 && maps[nx].charAt(ny) != 'X'){
                        dq.offer(new Node(nx, ny, cur.cost+1));
                    }
                }
            }
        }
        
        return -1;
    }
}