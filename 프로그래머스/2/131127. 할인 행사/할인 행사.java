import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        int n = discount.length - 10;
        
        // 원하는 제품 - 갯수 같이 저장
        HashMap<String, Integer> wMap = new HashMap<>();
        for (int i=0; i<want.length; i++){
            wMap.put(want[i], number[i]);
        }
        
        for (int i=0; i<=n; i++){
            HashMap<String, Integer> tMap = new HashMap<>(wMap);
            boolean flag = true;
            // 연속 10일 간 원하는 제품이 일치하는 경우만 카운트
            for(int j=i; j<i+10; j++){
                if(!tMap.containsKey(discount[j])){
                    flag = false; 
                    break;
                }
                int cnt = tMap.get(discount[j])-1;
                if(cnt==0) tMap.remove(discount[j]);
                else tMap.put(discount[j], cnt);
            }
            if(flag) answer ++;
        }
        
        return answer;
    }
}