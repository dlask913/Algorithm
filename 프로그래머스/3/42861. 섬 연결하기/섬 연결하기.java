import java.util.*;

class Node {
    int num, cost;
    
    Node(int num, int cost){
        this.num = num;
        this.cost = cost;
    }
}

class Solution {
    public int solution(int n, int[][] costs) {
        int answer = 0;
        int[] visited = new int[n];
        HashMap<Integer, List<Node>> hMap = new HashMap<>();
        PriorityQueue<Node> candidates =
            new PriorityQueue<>(Comparator.comparingInt(node->node.cost));
        
        // 1. 그래프 초기화 및 양방향 연결
        for(int i=0; i<n; i++){
            hMap.put(i, new ArrayList<>());
        }
        for(int[] cost : costs){
            hMap.get(cost[0]).add(new Node(cost[1], cost[2]));
            hMap.get(cost[1]).add(new Node(cost[0], cost[2]));
        }
        
        // 0번부터 시작
        int connected = 1;
        visited[0] = 1;
        candidates.addAll(hMap.get(0));
        
        // 2. 연결되는 노드들 중 가장 적은 비용 선택해서 방문 처리 -PRIM
        while(connected < n){
            Node next = candidates.poll(); // 최소 비용 노드 꺼내서 제거 
            
            if(visited[next.num] == 1) continue;
            
            answer += next.cost;
            visited[next.num] = 1;
            connected ++;
            
            for(Node candidate : hMap.get(next.num)){
                if(visited[candidate.num] == 0) {
                    candidates.add(candidate);
                }
            }
        }
        
        return answer;
    }
}