## [골1] 구간 합 구하기 (2042번)

https://www.acmicpc.net/problem/2042

### 문제 유형

자료 구조, 세그먼트 트리

<br>

### 어려웠던 점 / 문제의 핵심

세그먼트 트리를 구성하여 구간 합 연산 쿼리와 구간 업데이트 쿼리를 빠르게 처리하면 된다.

기본적인 세그먼트 트리 문제이다.

주의할 점은 입력으로 들어오는 수의 범위가 최대 long형이다. 초기 배열을 입력 받을 때, 그리고 업데이트 연산에서 `c`값을 long형으로 입력 받아야 에러가 나지 않는다. 

<br>

### 언어별 풀이 요약

| 언어            | 메모리    | 실행 시간(ms) | 시간복잡도       | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고            |
| --------------- | --------- | ------------- | ---------------- | ---------- | --------- | --------- | -------------------- |
| Python          |           |               |                  |            |           |           |                      |
| Java (세그먼트) | 105748 KB | 780 ms        | O((M + K) *logN) | O(N * 4)   | 40분      | 3         | :white_check_mark:   |
| Java (펜윅)     | 93728 KB  | 584 ms        | O((M + K) *logN) | O(N)       | 20분      | 2         | :white_large_square: |
| Kotlin          |           |               |                  |            |           |           |                      |

<br>

### 예외(테스트) 케이스

```
```
