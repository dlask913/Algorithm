import java.util.*;

class Song implements Comparable<Song> {
    int idx; 
    int play; 
    String genre;
    int playSum;
    
    public Song(int idx, int play, String genre, int playSum){
        this.idx = idx;
        this.play = play;
        this.genre = genre;
        this.playSum = playSum;
    }
    
    @Override
    public int compareTo(Song other){
        if(this.playSum != other.playSum){
            // other 가 더 크면 양수, 작으면 음수 -> 내림차순
            return Integer.compare(other.playSum, this.playSum);
        }
        return Integer.compare(other.play, this.play);
    }
    
    public void print(){
        System.out.printf("idx: %d, genre: %s, play: %d, sum: %d \n"
                           , idx, genre, play, playSum);
        
    }
}

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();
        int n = genres.length;
        HashMap<String, Integer> sMap = new HashMap<>();
        List<Song> playList = new ArrayList<>();
        
        // 각 장르의 총 재생된 횟수 구하기
        for(int i=0; i<n; i++){
            sMap.merge(genres[i], plays[i], Integer::sum);
        }
        
        // 장르 합 기준 내림차순, 같은 경우 횟수 기준 내림차순
        for(int i=0; i<n; i++){
            Song song = new Song(i, plays[i], genres[i], sMap.get(genres[i]));
            playList.add(song);
        }
        Collections.sort(playList);
        
        // 장르당 최대 2개까지만 출력
        HashMap<String, Integer> cMap = new HashMap<>();
        for(Song song : playList){
            int cnt = cMap.getOrDefault(song.genre, 0);
            if (cnt>=2) continue;
            
            cMap.merge(song.genre, 1, Integer::sum);
            answer.add(song.idx);
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}