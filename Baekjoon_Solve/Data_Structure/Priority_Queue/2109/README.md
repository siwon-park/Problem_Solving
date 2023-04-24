## [골3] 순회강연 (2109번)

[https://www.acmicpc.net/problem/2109]()

### 문제 유형

자료 구조, 그리디, 정렬, 우선순위 큐

<br>

### 어려웠던 점 / 문제의 핵심

p가 클수록, d가 작을수록 우선순위가 높은 우선순위 큐를 구성하여 그리디하게 총 비용을 계산한다.

만약 현재 대학에서 원하는 최대 일자 d에 이미 다른 대학에서의 강의 일정이 잡혀 있으면, d보다 작은 다른 일자를 선택해서 스케줄로 잡고, break하여 그리디하게 선택하면 된다. 이를 위해 visited 방문 배열을 사용하였다.

![image](https://user-images.githubusercontent.com/93081720/232427128-032a3a7a-0106-4449-aad2-7c62d17caa10.png)

<br>

### 언어별 풀이 요약

| 언어   | 메모리   | 실행 시간(ms) | 시간복잡도 | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고            |
| ------ | -------- | ------------- | ---------- | ---------- | --------- | --------- | -------------------- |
| Python |          |               |            |            |           |           |                      |
| Java   | 19940 KB | 308 ms        | O(NlogN)   | O(N)       | 20분      | 1         | :white_large_square: |
| Kotlin |          |               |            |            |           |           |                      |

<br>

### 예외(테스트) 케이스

```
```
