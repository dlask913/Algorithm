import java.util.*;
class Solution
{
    public int solution(int n, int a, int b)
    {
        int answer = fight(a,b,0);
        return answer;
    }
    
    public int fight(int a, int b, int cnt){
        if (a == b) return cnt;
        return fight((int)Math.ceil(a/2.0), (int)Math.ceil(b/2.0), cnt+1);
    }
}