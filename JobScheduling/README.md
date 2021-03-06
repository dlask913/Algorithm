### JobScheduling_bruteforce Algorithm_임나정

**1. JobScheduling_bruteforce**
 : n개의 작업, 각 작업의 수행시간 t_i, i=1, 2, 3, .., n , 그리고 m개의 동일한 기계가 주어질 때, 모든 작업이 가장 빨리 종료되도록 작업을 기계에 배정하는 문제이다. 단, 한 작업은 배정된 기계에서 연속적으로 수행되어야 하고 기계는 1번에 하나의 작업만을 수행한다. 

**2. 최적해와 근사해의 근사비율**

 : 근사해를 OPT'이라고 하고 , 최적해를 OPT라고 할 때, OPT' <= 2 X OPT 이다.

  실제로 작업별로 n[idx]개의 작업 수행시간을 1, 2, 3, 4, ..으로 가정했을 때 ,
* n= 4 일 때 근사해는 6, 최적해는 5
* n= 8 일 때 근사해는 20, 최적해는 18
* n=16 일 때 근사해는 72, 최적해는 68로 OPT' <= 2 X OPT 를 확인
* OPT'/OPT <= 2 로 근사비율은 2가 된다.

**3. 시간복잡도**
- 그리디 알고리즘 : n개의 작업을 배정해야하고, 배열 L을 탐색해야하므로 n X O(m) + O(m) = O(nm) 
- 브루트포스 알고리즘 : O(경우의 수 X 각 경우에 대한 연산 횟수)

**4. 코드구현**
* `greedy()` : 현재까지 배정된 작업에 대해서 가장 빨리 끝나는 기계에 새 작업 배정
* `bruteforce()` : 경우의 수를 다 따져서 작업 배정
* `main()` : 수행시간 랜덤 출력 및 작업갯수에 따른 함수호출

**5. 성능분석**

![20210518230028](https://user-images.githubusercontent.com/79985588/118665073-f8f7e700-b82c-11eb-8209-2bcfcd350bf5.png)
* 브루트포스로 구현할 경우 최적해를 구할 수 있지만 그에 따라 걸리는 시간이 길어진다
* 그리디 알고리즘으로 구현할 경우 최적해와 근접한 근사해를 구할 수 있고 걸리는 시간이 짧다



**6. 실행결과**


![KakaoTalk_20210518_221732033](https://user-images.githubusercontent.com/79985588/118661574-3149f600-b82a-11eb-896e-24a3761006e9.png)