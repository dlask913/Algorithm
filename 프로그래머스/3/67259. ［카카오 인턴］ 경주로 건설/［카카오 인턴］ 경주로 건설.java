import java.util.*;
// 0,0 -> N-1, N-1
// 방향이 같을 때는 100원, 방향을 바꿀 때는 600원
class Node{
    int x,y,cost;
    int direction;
    Node(int x, int y, int cost){
        this.x = x;
        this.y = y;
        this.cost = cost;
    }
    void setDirection(int direction){
        this.direction = direction;
    }
    
    public void print(){
        System.out.printf("x, y, cost = %d, %d, %d \n", this.x, this.y, this.cost);
    }
}

class Solution {
    int[] dx = new int[]{1,-1,0,0};
    int[] dy = new int[]{0,0,1,-1};
    public int solution(int[][] board) {
        int answer = Integer.MAX_VALUE;
        int n = board.length;
        PriorityQueue<Node> pq = 
            new PriorityQueue<>(Comparator.comparingInt(node -> node.cost));
        int[][][] visited = new int[n][n][4];
        
        pq.offer(new Node(0,0,0));
        while(!pq.isEmpty()){
            Node cur = pq.poll();
            visited[cur.x][cur.y][cur.direction] = 1;

            if(cur.cost>answer) continue;
            
            if(cur.x == n-1 && cur.y == n-1){
                answer = Math.min(cur.cost, answer);
            }
            
            for(int i=0; i<4; i++){
                int nx = cur.x+dx[i];
                int ny = cur.y+dy[i];
                if(0<= nx && nx<n && 0<=ny && ny<n && board[nx][ny]==0 && visited[nx][ny][i]==0){
                    int cost;
                    if(cur.x==0 && cur.y==0) cost = 100; // 출발점
                    else if(cur.direction==i) cost = 100; // 같은 방향
                    else cost = 600; // 다른 방향
                    
                    Node next = new Node(nx, ny, cur.cost+cost);
                    next.setDirection(i);
                    pq.offer(next);
                }
            }
        }
        
        return answer;
    }
}