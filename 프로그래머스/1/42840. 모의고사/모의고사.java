import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int n = answers.length;
        int[][] numbers = {
            {1,2,3,4,5},
            {2,1,2,3,2,4,2,5},
            {3,3,1,1,2,2,4,4,5,5}
        };

        int[] scores = {0, 0, 0};
        for(int i=0; i<n; i++){
            for (int j=0; j<3; j++){
                int k = i % numbers[j].length;
                if(answers[i] == numbers[j][k]){
                    scores[j] += 1;
                }
            }
        }
        
        int maxScore = Arrays.stream(scores).max().getAsInt();
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i=0; i<3; i++){
            if(scores[i]==maxScore){
                answer.add(i+1);
            }
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}