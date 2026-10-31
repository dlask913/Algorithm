import java.util.*;

class Solution {
    int[] apeach = new int[11];
    int maxDiff = -1;
    int[] answer = {-1};
    
    public int[] solution(int n, int[] info) {
        int[] visited = new int[11];
        for(int i=0; i<=10; i++){
            apeach[i] = info[10-i];
        }
        calculateScores(n, 10, visited, 0);
        return answer;
    }
    
    void calculateScores(int arr, int start, int[] visited, int lionScore){
        // 해당 과녁에서 어피치보다 많이 화살을 가져갈 수 있는 경우 
        for(int i=start; i>=0; i--){
            int neadArr = apeach[i]+1;
            if(arr >= neadArr){
                visited[i] = neadArr;
                calculateScores(arr-neadArr, i-1, visited, lionScore+i);
                visited[i] = 0;
            }
        }
        
        // 어피치 점수 계산해서 최고 차이 점수 갱신된 경우 answer 업데이트
        int apeachScore = 0;
        int currentDiff = 0;
        for(int i=10; i>=0; i--){
            if(apeach[i] > visited[i]) apeachScore += i;
        }
        currentDiff = lionScore-apeachScore;
        
        if(currentDiff > 0 && maxDiff <= currentDiff){
            int[] tmp = new int[11];
            for(int i=10; i>=0; i--){
                if(i==0) tmp[10-i] = visited[i] + arr;
                else tmp[10-i] = visited[i];
            }
            
            // 가장 낮은 점수를 맞힌경우 구하기
            if(maxDiff == currentDiff){
                for(int i=10; i>=0; i--){
                    if(tmp[i] == answer[i]) continue;
                    
                    if(tmp[i] > answer[i]){
                        answer = tmp;
                    }
                    break;
                }
            } else {
                answer = tmp;
                maxDiff = currentDiff;
            }
        }
    }
}