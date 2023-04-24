## [골1] 수들의 합 7 (2268번)

https://www.acmicpc.net/problem/2268

### 문제 유형

자료 구조, 세그먼트 트리

<br>

### 어려웠던 점 / 문제의 핵심

sum, update 연산이 가능한 구간합을 구할 수 있는 세그먼트 트리를 구현하여 주어지는 쿼리에 대해 응답하면 된다.

단, 주의할 점은 `j < i`인 경우 sum 함수는 `A[j] + A[j + 1] + A[j + 2] + ... + A[i]`를 구해야 한다는 점이다.

또한 `k`의 최댓값이 10만이기 때문에 `long`형으로 선언해야 한다.

<br>

### 언어별 풀이 요약

| 언어   | 메모리    | 실행 시간(ms) | 시간복잡도 | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고            |
| ------ | --------- | ------------- | ---------- | ---------- | --------- | --------- | -------------------- |
| Python |           |               |            |            |           |           |                      |
| Java   | 336924 KB | 1596 ms       | O(MlogN)   | O(N)       | 40분      | 2         | :white_large_square: |
| Kotlin |           |               |            |            |           |           |                      |

<br>

### 예외(테스트) 케이스

```
```
