import java.io.IOException;
import java.util.Random;
import java.util.Scanner;

public class Bubble_Sort {

    private void input(int[] A) {
        Random r = new Random();
        for (int i = 0; i < A.length; i++) {
            A[i] = r.nextInt(10000) + 1;
            if (i != 0) {
                int j = 0;
                while (j < i) {
                    if (A[j++] == A[i]) i--;
                }
            }
        }
        for (int k : A) System.out.print(k + ", ");
        System.out.println();
    }

    private int[] Bubble(int[] A){
        int a = 0;
        for ( int i = 1; i<A.length;i++){
            for ( int j=1;j<=(A.length-i);j++){ // i가 돌아가는 포문이 한 번 수행될 때 마다 마지막 값이 정해짐
                if(A[j-1]>A[j]){ // 이웃한 원소보다 A[j]가 더 작을 때
                    // 값 바꿔 저장하기
                    a = A[j-1];
                    A[j-1] = A[j];
                    A[j] = a;
                }
            }
        }
        return A;
    }

    public static void main(String[] args) throws IOException {

        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] A = new int[n];
        Bubble_Sort bubble = new Bubble_Sort();
        bubble.input(A);
        bubble.Bubble(A);
        for (int k : A) System.out.print(k + ", ");

    }
}
