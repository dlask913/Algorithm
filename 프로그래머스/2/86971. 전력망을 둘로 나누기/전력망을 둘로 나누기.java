import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        int wLen = wires.length;
        
        for(int i=0; i<wLen; i++){
            // 1. 하나의 간선을 끊은 상태의 그래프 생성
            Map<Integer, List<Integer>> graph = new HashMap<>();
            for(int j=0; j<wLen; j++){ 
                if(i==j) continue;
                graph.computeIfAbsent(wires[j][0], key -> new ArrayList<>()).add(wires[j][1]);
                graph.computeIfAbsent(wires[j][1], key -> new ArrayList<>()).add(wires[j][0]);
            }
            
            // 2. 네트워크의 송전탑 개수 차이 구하기
            int[] visited = new int[n+1];
            int[] nCnt = new int[]{-1, -1};
            for(int k=1; k<=n; k++){
                if(visited[k]==0) {
                    int cnt = dfs(k, graph, visited);
                    
                    if(nCnt[0] == -1) nCnt[0] = cnt;
                    else nCnt[1] = cnt;
                }
            }
            answer = Math.min(Math.abs(nCnt[0]-nCnt[1]), answer);
        }
        return answer;
    }
    
    int dfs(int pos, Map<Integer, List<Integer>> network, int[] visited){
        visited[pos] = 1;
        int cnt = 1;

        List<Integer> candidates = network.get(pos);
        if(candidates != null){
            for(int cand : candidates){
                if(visited[cand] == 0) {
                    cnt += dfs(cand, network, visited);
                }
            }
        }
        
        return cnt;
    }
}