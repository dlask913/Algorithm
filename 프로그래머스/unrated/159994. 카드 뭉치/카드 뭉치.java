class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "No";
        int i=0,j=0,g=0;
        boolean flag=true;
        while(true){
            if((g==goal.length) || (i==cards1.length && j==cards2.length)) break;
            
            if(i<cards1.length && goal[g].equals(cards1[i])){
                i++;
                g++;
            }else if(j<cards2.length && goal[g].equals(cards2[j])){
                j++;
                g++;
            } else {
                flag = false;
                break;
            }
        }
        if(flag){
            answer="Yes";
        }
        return answer;
    }
}