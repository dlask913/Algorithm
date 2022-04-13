import java.util.Random;
import java.util.Scanner;

public class Dijkstra {

    // 가중치 그래프 만들기
    private void Init(int[][] A){
        Random r = new Random();
        for(int i=0;i<A.length;i++){
            for(int j=0;j<A.length;j++){
                if(i==j) A[i][j]=0;
                else A[i][j]=A[j][i]=r.nextInt(10)+1;
            }
        }
        // 가중치그래프 출력
        System.out.println("------------------------");
        for(int i=0;i<A.length;i++){
            for(int j=0;j<A.length;j++){
                System.out.print(A[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println("------------------------");
    }

    // 최소 경로 찾아 저장하기
    private void Shortestpath(int[][] A,int[] D, int s,int q) {
        int n = 0,i=0;
        while (n <= q) { // 경유하기 전 연결되어있는 점들과의 거리 배열 D에 담아주기
            D[n] = A[s][n]; // = A[s][i] -> 여기서 s는 출발점 위치
            n++;
        }
        // 최소거리 갱신하는 함수 index별로 호출
        while(i<=q){
            Update(A, D, i);
            i++;
        }
    }

    // 최소거리 갱신
    private void Update(int[][] A, int[] D,int idx){
        for(int i=0;i<D.length;i++){
            if ((i != 0) && (i != idx)){
                if((D[idx]+A[idx][i])<D[i]) D[i]=D[idx]+A[idx][i];
            }
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("점의 개수를 입력하세요 : ");
        int size = scan.nextInt(); // size 입력받기 ( 점의 수 )
        int[][]G = new int[size][size]; // 가중치 그래프 배열 G
        Dijkstra sh = new Dijkstra();
        sh.Init(G); // 그래프 초기화
        int n = G.length; // 점의 수
        int[] D = new int[n]; // 입력받은 점을 기준으로 각 점들까지의 최소거리 저장하는 배열
        sh.Shortestpath(G,D,0,n-1); // 실행
        // 출력
        for ( int i =0;i<D.length;i++){
            System.out.println("출발점(1행 1열)에서 "+i+"까지의 최소거리 ==> "+ D[i]);
        }
    }
}
