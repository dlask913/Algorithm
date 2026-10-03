import java.util.*;

class Solution {
    HashMap<Integer, List<Integer>> hMap = new HashMap<>();
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int[] visited = new int[n];
        
        // 1. 그래프 초기화
        for(int i=0; i<n; i++){
            hMap.put(i, new ArrayList<>());
        }
        for (int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(i!=j && computers[i][j]==1){
                    hMap.get(i).add(j);
                }
            }
        }
        
        // 2. 그래프 탐색
        for(int i=0; i<n; i++){
            if(visited[i] == 0){
                dfs(i, visited);
                answer ++;
            }
        }
        
        return answer;
    }
    
    void dfs(int cur, int[] visited){
        List<Integer> candidates = hMap.get(cur);
        visited[cur] = 1;
        
        for(int next : candidates){
            if(visited[next] == 0){
                dfs(next, visited);
            }
        }
    }
}