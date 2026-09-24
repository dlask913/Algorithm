import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> pMap = new HashMap<>();
        for(String part : participant){
            // 키가 없으면 1 있으면 +1, O(1)
            pMap.merge(part, 1, Integer::sum); 
        }
        
        for(String comp : completion){
            // null 을 반환하면 key 가 자동으로 삭제됨
            pMap.computeIfPresent(comp, (key, value) -> {
                return value == 1 ? null : value-1;
            });
        }
        
        // 남아있는 key 반환
        return pMap.keySet().iterator().next();
    }
}