import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int n = numbers.length;
        HashSet<Integer> hs = new HashSet<>();
        
        for (int i=0; i<n; i++){
            for (int j=i+1; j<n; j++){
                hs.add(numbers[i]+numbers[j]);
            }
        }
        
        return hs.stream().sorted().mapToInt(Integer::intValue).toArray();
    }
}