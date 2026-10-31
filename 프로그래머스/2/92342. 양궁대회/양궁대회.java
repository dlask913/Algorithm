import java.util.*;

class Solution {
    int[] apeach = new int[11];
    int maxDiff = 0;
    int[] answer = {-1};
    
    public int[] solution(int n, int[] info) {
        int[] visited = new int[11];
        for(int i=0; i<=10; i++){
            apeach[i] = info[10-i];
        }
        calculateScores(n, visited, 0);
        return answer;
    }
    
    void calculateScores(int arr, int[] visited, int lionScore){
        // 해당 과녁에서 어피치보다 많이 화살을 가져갈 수 있는 경우 
        for(int i=10; i>=0; i--){
            int apeachArr = apeach[i];
            if(arr>apeachArr && visited[i] == 0){
                visited[i] = apeachArr+1;
                calculateScores(arr-(apeachArr+1), visited, lionScore+i);
                visited[i] = 0;
            }
        }
        
        // 어피치 점수 계산해서 최고 차이 점수 갱신된 경우 answer 업데이트
        int apeachScore = 0;
        for(int i=10; i>=0; i--){
            if(apeach[i] > visited[i]) apeachScore += i;
        }
        
        if((lionScore > apeachScore) && maxDiff <= (lionScore-apeachScore)){ 
            maxDiff = lionScore-apeachScore;
                                   
            int[] tmp = new int[11];
            for(int i=10; i>=0; i--){
                if(i==0) tmp[10-i] = visited[0] + arr;
                else tmp[10-i] = visited[i];
            }
            answer = tmp;
        }
    }
}