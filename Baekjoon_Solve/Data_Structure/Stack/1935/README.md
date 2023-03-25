## [실3] 후위 표기식2 (1935번)

https://www.acmicpc.net/problem/1935

### 문제 유형

자료 구조, 스택

<br>

### 어려웠던 점 / 문제의 핵심

스택의 원리를 이용해서, 연산자가 들어왔을 때, 스택의 요소를 2개 뽑아서 연산 결과를 다시 스택에 집어 넣는 과정을 반복하면 된다.

각 문자에 해당하는 숫자는 Map 자료형을 쓰면 된다.

#### int → char 형 변환

```java
char s = (char) (65 + '0');
char s = (char) (n + i);
```

#### 소수점 출력

```java
System.out.printf("%.2f", ans);
```

<br>

### 언어별 풀이 요약

| 언어   | 메모리   | 실행 시간(ms) | 시간복잡도 | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고            |
| ------ | -------- | ------------- | ---------- | ---------- | --------- | --------- | -------------------- |
| Python |          |               |            |            |           |           |                      |
| Java   | 14616 KB | 132 ms        | O(N)       | O(N)       | 30분      | 1         | :white_large_square: |
| Kotlin |          |               |            |            |           |           |                      |

<br>

### 예외(테스트) 케이스

```
```
