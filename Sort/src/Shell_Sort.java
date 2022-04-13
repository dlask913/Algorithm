import java.util.Random;
import java.util.Scanner;


public class Shell_Sort {
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

    private int[] Shell(int[] A ){
        int current = 0;
        for (int h = A.length; h>=1; h=h/2) { // 간격은 점점 반으로 줄어듦
            for (int i = h; i < A.length; i++) {
                current = A[i];
                int j = i;
                while (j >= h && A[j - h] > current) {
                    A[j] = A[j-h];
                    j = j-h;
                }
                A[j]=current;
            }
        }
        return A;
    }

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] A = new int[n];
        Shell_Sort shell = new Shell_Sort();
        shell.input(A);
        shell.Shell(A);
        for (int k : A) System.out.print(k + ", ");

    }
}
