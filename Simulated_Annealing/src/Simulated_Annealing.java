import java.util.ArrayList;
import java.util.Random;

public class Simulated_Annealing {
    // 임의의 4차 방정식
    private static double calculate(double x ){
        return -0.51*x*x*x*x+21*x*x*x+22*x+109;
    }
    private static double SA(double s, double t, double a, int lower , int upper , ArrayList hist){
        Random r = new Random();
        double s0 = r.nextDouble()*(upper-lower)+lower;
        double f0 = calculate(s0);
        hist.add(f0);
        for ( int i = 0; i<t; i++){
            int kt = (int) Math.round(s * 20);
            for (int j = 0; j<kt;j++) {
                double s1 = r.nextDouble() * (upper - lower) + lower;
                double f1 = calculate(s1);
                double d = f1 - f0;
                if (d > 0) {
                    s0 = s1;
                    f0 = f1;
                    hist.add(f0);
                } else {
                    double q = r.nextDouble();
                    double p = Math.exp(-d / s);
                    if (q < p) {
                        s0 = s1;
                        f0 = f1;
                        hist.add(f0);
                    }
                }
            }
            s = a*s;
        }
        return s0;
    }
    public static void main(String[] args) {
        double s = 1 ; // 초기 후보해
        double t = 100 ; // 종료조건
        double a = 0.98; // 냉각률
        ArrayList<ArrayList> hist = new ArrayList<>();
        Simulated_Annealing sa = new Simulated_Annealing();
        sa.SA(s,t,a,0,40,hist); // x는 0~40으로 제한
        System.out.println(hist);
    }
}