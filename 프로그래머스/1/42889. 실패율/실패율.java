import java.util.*;
class Solution {
    public int[] solution(int N, int[] stages) {
        double[] rate = new double[N];
        HashMap<Integer, Double> rates = new HashMap<>();
        int[] scores = new int[N];
        
        // 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 카운트
        for (int i=0; i<stages.length; i++){
            if(stages[i]>N) continue;
            scores[stages[i]-1]++;
        }
        
        // 실패율 구하기
        double stageLen = stages.length; 
        for(int i=0; i<N; i++){
            if (stageLen == 0) rates.put(i+1, 0.0); // NaN 예방 (분모 0인 경우)
            else rates.put(i+1, scores[i] / stageLen);
            stageLen -= scores[i];
        }
        System.out.print(rates);
        
        // 실패율 내림차순, 실패율이 같으면 작은 번호 먼저 return 
        return rates.entrySet().stream().sorted((o1, o2) -> o1.getValue().equals(o2.getValue()) 
                ? Integer.compare(o1.getKey(), o2.getKey()) : Double.compare(o2.getValue(), o1.getValue()))
            .mapToInt(HashMap.Entry::getKey).toArray();
    }
}