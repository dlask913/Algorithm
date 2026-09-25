import java.util.*;

class Person {
    String name; // seller
    int money; 
    String refName; // referral 
    
    Person (String name, String refName){
        this.name = name; 
        this.money = 0; 
        this.refName = refName.equals("-") ? "center" : refName;
    }
    
    void print(){
        System.out.printf("name: %s, money: %d, refName:%s \n", name, money, refName);
    }
}
class Solution {
    HashMap<String, Person> eMap = new HashMap<>();
    
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        int n = enroll.length;
        int[] answer = new int[n];
        
        // Person 리스트로 정리 
        for(int i=0; i<n; i++){
            Person person = new Person(enroll[i], referral[i]);
            eMap.put(enroll[i], person);
        }
        
        // 이익 계산
        for(int i=0; i<seller.length; i++){
            calculateAmmount(seller[i], amount[i]*100);
        }
        
        // 이익 정리
        for(int i=0; i<n; i++){
            answer[i] = eMap.get(enroll[i]).money;
        }
        return answer;
    }
     
    void calculateAmmount(String seller, int amount){
        Person person = eMap.get(seller);
        int profit = (int)(amount*0.1);
        person.money += (amount-profit);
        
        if(person.refName.equals("center") || amount == 0) return;
        calculateAmmount(person.refName, profit);
    }
}