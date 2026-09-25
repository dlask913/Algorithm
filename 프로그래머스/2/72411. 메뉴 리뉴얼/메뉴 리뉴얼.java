import java.util.*;

class Solution {
    public String[] solution(String[] orders, int[] course) {
        List<String> answer = new ArrayList<>();
        int n = orders.length;
        HashMap<String, Integer> result = new HashMap<>();
        HashMap<Integer, Integer> maxMap = new HashMap<>();
        
        // 1. 모든 조합 구하기
        for (String order : orders){
            char[] chars = order.toCharArray();
            Arrays.sort(chars);
            dfs(new String(chars), 0, "", result);
        }
        
        // 2. 각 course 별 max 값 구하기
        for (int c : course){
            maxMap.put(c, 0);
        }
        for (Map.Entry<String, Integer> entry : result.entrySet()){
            int keyLen = entry.getKey().length();
            int value = entry.getValue();
            if(!maxMap.containsKey(keyLen)) continue;
            
            maxMap.merge(keyLen, value, Math::max);
        }
        
        // 3. 조건에 맞는 course 구하기
        for (Map.Entry<String, Integer> entry : result.entrySet()){
            String key = entry.getKey();
            int value = entry.getValue();
            if(value >= 2 && maxMap.getOrDefault(key.length(),-1) == value) {
                answer.add(key);
            }
        }
        Collections.sort(answer);
        
        return answer.toArray(new String[0]);
    }
    
    void dfs(String str, int start, String current, HashMap<String, Integer> result) {
        if(current.length() > 1){
            result.merge(current, 1, Integer::sum);
        }
        
        for(int i=start; i<str.length(); i++){
            dfs(str, i+1, current + str.charAt(i), result);
        }
    }
}