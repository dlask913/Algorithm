import java.util.*;
// 최소 필요도 확인하고 탐험 이후 소모 피로도만큼 마이너스
// return 하루동안 탐험할 수 있는 최대 던전 수
class Solution {
    int answer = -1;
    public int solution(int k, int[][] dungeons) {
        int[] visited = new int[dungeons.length];
        
        Arrays.sort(dungeons, (a,b) -> {
            if(a[0] != b[0]){
                return Integer.compare(b[0], a[0]); // 최소 필요도 내림차순
            } 
            return Integer.compare(a[1], b[1]); // 소모 필요도 오름차순
        });
        
        explore(k, dungeons, visited, 0);
            
        return answer;
    }
    
    void explore(int fatigue, int[][] dungeons, int[] visited, int cnt){
        answer = Math.max(cnt, answer);
        
        for(int i=0 ;i<dungeons.length; i++){
            if(visited[i] == 0 && fatigue>=dungeons[i][0]){
                visited[i] = 1;
                explore(fatigue-dungeons[i][1], dungeons, visited, cnt+1);
                visited[i] = 0;
            }
        }
    }
    
}