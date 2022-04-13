import java.util.*;
import static javax.swing.UIManager.get;
public class JobScheduling_Greedy {

    public static void main(String[] args) {
        Random r = new Random();
        Scanner scan = new Scanner(System.in);
        int n = 10; //scan.nextInt(); // 작업의 갯수 입력받기
        int s=0,f=0;
        List<JobS> L = new ArrayList<>();
        JobScheduling_Greedy job = new JobScheduling_Greedy();

        for (int i=0;i<n;i++){
            s = r.nextInt(10)+1;
            f = r.nextInt(10)+1;
            if(s>=f) i--;    // 시작시간이 종료시간보다 크거나 같으면 i --;
            else        L.add(new JobS(s,f)); // 생성된 작업 저장
        }

        Collections.sort(L,new JobSComparator()); // 시작시간을 기준으로 오름차순 정렬
        System.out.println(L); // 정렬된 리스트 L 출력
        ArrayList<ArrayList> M = new ArrayList<ArrayList>();

        int flag = 0;
        int idx = 0;
        int cnt = 0;

        while(!(L.isEmpty())){
            int s_idx = L.get(idx).getS()-1; // 시작시간 index
            int f_idx = L.get(idx).getF()-1; // 종료시간 index
            ArrayList<String> S = new ArrayList<String>();
            for(int k = 0 ; k<10 ; k ++) S.add(null); // 작업시간 0~9로 임의지정 & 초기화
            // 작업시간 할당
            for (int j = 0; j < 10; j++) {
                if(j >= s_idx && j <= f_idx)  S.set(j, "task" + (cnt + 1));
                else                          S.set(j, null);
            }
            if(cnt == 0) {   M.add(0,S); } // 첫 번째 작업 첫 번째 기계에 저장
            else{
                int index = -1;
                for(int l=0;l<M.size();l++){
                    flag = 0;
                    for (int i = s_idx; i<f_idx;i++){
                        if ((M.get(l).get(i)==null) && !(S.get(i)==null)) {   flag++; }
                    }
                    if (flag == (f_idx - s_idx)) {
                        index = l;
                        break; }
                }
                if(index >= 0){
                    for (int p =s_idx ; p<=f_idx; p++)   M.get(index).set(p, "task"+(cnt+1));
                }
                else { M.add(S); }
            }
            L.remove(idx); // 할당된 작업 삭제
            cnt++;
        }
        //출력
        for (int l =0;l<M.size();l++)    System.out.println("Machine"+(l+1)+" => "+M.get(l));
        System.out.println("최적해는 " +M.size()+"대의 기계에 위와 같이 배정하는 것이다.");
    }
}

// list를 정렬하기 위한 class 생성
class JobS{
    private int s;
    private int f;
    public JobS(int s, int f) {
        this.s = s;
        this.f = f;
    }
    public void setF(int f) { this.f = f; }
    public void setS(int s) { this.s = s; }
    public int getS() { return s;}
    public int getF() { return f;}
    @Override
    public String toString(){
        return "["+s+","+f+"]";
    }
}

// 시작시간 기준으로 작업들 오름차순 정렬
class JobSComparator implements Comparator<JobS>{
    @Override
    public int compare(JobS o1, JobS o2) {
        if(o1.getS()>o2.getS()) return 1;
        if(o1.getS()<o2.getS()) return -1;
        return 0;
    }
}
