import java.util.Random;
import java.util.Scanner;

public class Selection_Sort {
    // 값 저장 & 중복 제거
    private void input(int[] A){
        Random r = new Random();
        for (int i=0;i<A.length;i++){
            A[i]=r.nextInt(10000)+1;
            if(i != 0){
                int j = 0;
                while(j<i) {
                    if(A[j++] ==A[i]) i --;
                }
            }
        }
        for (int k : A) System.out.print(k + ", ");
        System.out.println();
    }

    private int[] Selection(int[] A){
        int a = 0;
        for (int i = 0; i<A.length-1; i++){
            int min = i ;
            for ( int j =i+1;j<A.length;j++) {
                if (A[j] < A[min]) {  // A[i+1] ~ A[A.length-1]과 A[i] 를 비교해서 전자가 더 작을 경우
                    min = j; // 가장 최소값을 가지는 index를 min에 저장
                }
            }
            // 값 바꿔 저장하기
            a=A[i];
            A[i] = A[min];
            A[min] = a;
        }
        return A;
    }

    public static void main(String[] args){

        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] A = new int[n];
        Selection_Sort selection = new Selection_Sort();
        selection.input(A);
        selection.Selection(A);
        for (int k : A) System.out.print(k + ", ");

    }
}
