import java.util.*;
class Solution {
    public String[] solution(String[] record) {
        ArrayList<String> answer = new ArrayList<>();
        HashMap<String, String> rMap = new HashMap<>();
        
        for(String str : record){
            String[] part = str.split(" ");
            if(part[0].equals("Leave")) continue;
            rMap.put(part[1], part[2]);
        }
        
        for(String str : record){
            String[] part = str.split(" ");
            switch(part[0]) {
                case "Enter":
                    answer.add(rMap.get(part[1])+"님이 들어왔습니다.");
                    break;
                case "Leave":
                    answer.add(rMap.get(part[1])+"님이 나갔습니다.");
                    break;
            }
        }
        
        return answer.toArray(new String[0]);
    }
}