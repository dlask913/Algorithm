import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        Set<Integer> hSet = Arrays.stream(nums).boxed()
            .collect(Collectors.toSet());
        answer = Math.min(nums.length/2, hSet.size());
        return answer;
    }
}