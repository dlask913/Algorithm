### 모의담금질을 이용한 parameter estimation

**1. 모의담금질 기법 구현**

탐색 공간에서 주어진 함수의 전역 최적점(global optimum)의 좋은 근사치를 찾는 확률적 휴리스틱 접근 방식을 말하며 구현내용은 수업시간 코드 구현 내용에서 다른 함수를 응용하였습니다.

**2. 모델 선정**


![그림1](https://user-images.githubusercontent.com/79985588/121346258-defb8100-c960-11eb-906c-1b466c0144f4.png)

모델은 남자 표준 체중 계산 공식인 y = 50+2.3(0.4x-60)으로 하였습니다.
// y = 0.92x-88


**3. 성능분석 및 결과**

![Figure_1](https://user-images.githubusercontent.com/79985588/121347916-b07ea580-c962-11eb-95f3-c8869643fab2.png)

먼저 그래프를 통해 데이터에 따른 최적화 함수를 확인하였습니다.

![20210609201938](https://user-images.githubusercontent.com/79985588/121345831-4c5ae200-c960-11eb-89e9-6d0898dea87f.png)

또한 위의 데이터를 바탕으로 모의담금질 기법을 이용하여 추정한 결과 y=0.92x-88과 매우 흡사한 결과를 확인할 수 있었습니다.  
비선형모델을 탐색하여 추정하고싶었는데 잘 와닿지않아 선형모델을 선택하였습니다. 
그래서 오차범위가 매우 적고 다항식의 차수가 높아질수록 오차범위도 늘고 성능분석도 정확히 할 수 있지 않을까 생각했습니다. 
