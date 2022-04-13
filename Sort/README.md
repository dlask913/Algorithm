
**1. 정렬 알고리즘의 종류**
#### *Bubble Sort : 이웃하는 숫자를 비교하여 작은 수를 앞쪽으로 이동시키는 과정을 반복하여 정렬하는 알고리즘
#### *Selection Sort  : 입력 배열 전체에서 최솟값을 '선택'하여 배열의 0번 원소와 자리를 바꾸고 다음에는 0번 원소를 제외한 나머지 원소에서 최솟값을 선택하여 배열의 1번 원소와 자리를 바꾸고 이러한 방식으로 마지막에 2개의 원소 중에서 작은 값을 선택하여 자리를 바꿈으로써 오름차순의 정렬을 마침
#### *Insertion Sort : 배열을 정렬된 부분(앞부분)과 정렬이 안 된 부분(뒷부분)으로 나누고 정렬이 안 된 부분의 가장 왼쪽 원소를 정렬된 부분의 적절한 위치에 삽입하여 정렬되도록 하는 과정을 반복
#### *Shell Sort : 삽입 정렬을 이용하여 배열 뒷부분의 작은 숫자를 앞부분으로 빠르게 이동시키고 동시에 앞부분의 큰 숫자는 뒷부분으로 이동시키며 가장 마지막에는 삽입 정렬을 수행

**2. 코드구현**
##### `input()` : 배열 안의 값을 랜덤으로 저장 및 중복 제거
##### `Bubble()`, `Selection()`, `Insertion()`, `Shell()` : 각각의 정렬을 수행
##### `main()` : 배열의 사이즈를 입력받아 여러 함수를 호출시켜 결과값을 출력

**3. 실행결과**

![20210504233422](https://user-images.githubusercontent.com/79985588/117020295-46eef400-ad31-11eb-8108-92cbdada5829.png)


**4. 성능분석**


![Bubble_Sort](https://user-images.githubusercontent.com/79985588/117014337-a9dd8c80-ad2b-11eb-99b7-798727c6127f.png)
![Insertion_Sort](https://user-images.githubusercontent.com/79985588/117014324-a813c900-ad2b-11eb-979e-ced80909403a.png)
![Selection_Sort](https://user-images.githubusercontent.com/79985588/117014331-a944f600-ad2b-11eb-922a-cfe6f20a2561.png)
![Shell_Sort](https://user-images.githubusercontent.com/79985588/117014333-a944f600-ad2b-11eb-9a36-534b0767e2a0.png)

**5. 결론**
: Shell Sort의 입력 값에 따라 걸리는 시간이 가장 짧습니다.