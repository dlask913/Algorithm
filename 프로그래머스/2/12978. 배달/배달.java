import java.util.*;
class Node{
    int num, cost;
    
    Node(int num, int cost){
        this.num = num;
        this.cost = cost;
    }
}
// 시작점은 항상 1번 마을
// 다른 마을로 가기 위한 최소 비용 구하기
class Solution {
    public int solution(int N, int[][] roads, int K) {
        int answer = 0;
        HashMap<Integer, List<Node>> hMap = new HashMap<>();
        int[] dist = new int[N+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        
        // 그래프 초기화
        for(int i=1; i<=N; i++){
            hMap.put(i, new ArrayList<>());
        }
        for(int[] road : roads){
            hMap.get(road[0]).add(new Node(road[1], road[2]));
            hMap.get(road[1]).add(new Node(road[0], road[2]));
        }
        
        // 최소 비용 구하기
        Deque<Integer> dq = new ArrayDeque<>();
        dq.offer(1);
        dist[1] = 0;
        
        while(!dq.isEmpty()){
            int cur = dq.poll();
            
            List<Node> candidates = hMap.get(cur);
            for(Node next : candidates){
                int nextCost = dist[cur] + next.cost;
                if (nextCost < dist[next.num]) { // 거리가 더 작은 경우만
                    dist[next.num] = nextCost;
                    dq.offer(next.num);
                }
            } 
        }
        
        for(int i=1;i<=N;i++){
             if(dist[i] <= K) answer ++;
        }

        return answer;
    }
}