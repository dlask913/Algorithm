import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        HashSet<String> reportSet = new HashSet(Arrays.asList(report));
        HashMap<String, Integer> stopMap = new HashMap<>();
        HashMap<String, Integer> idMap = new HashMap<>();

        // 중지 회원 찾기
        for(String rep : reportSet){
            String[] part = rep.split(" ");
            stopMap.merge(part[1], 1, Integer::sum);
        }
        stopMap.entrySet().removeIf(entry -> entry.getValue() < k);

        // 신고 회원 찾기
        for (int i=0; i<id_list.length; i++) {
           idMap.put(id_list[i], i);
        }
        for(String rep : reportSet){
            String[] part = rep.split(" ");
            if(!stopMap.containsKey(part[1])) continue;
            answer[idMap.get(part[0])] ++;
        }
        
        return answer;
    }
}