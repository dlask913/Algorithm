import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int n = progresses.length;
        int[] deploy = new int[n+1];
        Deque<Integer> answer = new ArrayDeque<>();
        
        // 1. 기능별 배포 가능한 날짜 계산
        for(int i=0; i<n; i++){
            int days = (100-progresses[i])/speeds[i];
            if((100-progresses[i])%speeds[i] != 0) days ++;
            
            if(i==0) deploy[i] = days;
            else deploy[i] = Math.max(days, deploy[i-1]);
        }
        
        // 2. 날짜에 따라 가능한 기능 수 세기
        int cnt = 1;
        for(int i=0; i<n; i++){
            if(deploy[i] == deploy[i+1]) cnt++;
            else {
                answer.add(cnt);
                cnt = 1;
            }
        }
        
        return answer.stream().mapToInt(Integer::intValue)
            .toArray();
    }
}