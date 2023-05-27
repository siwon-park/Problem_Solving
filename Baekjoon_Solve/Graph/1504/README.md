## [골4] 특정한 최단 경로 (1504번)

[https://www.acmicpc.net/problem/1504]()

### 문제 유형

그래프 이론, 다익스트라

<br>

### 어려웠던 점 / 문제의 핵심

v1과 v2를 반드시 지나는 최단 경로를 찾아야 하므로, 이 두 지점을 지나는 경로 중 최솟값을 찾아 반환하면 된다.

v1과 v2를 지나는 경우는 다음과 같다.

- 1 -> v1, v1 -> v2, v2 -> N
- 1 -> v2, v2 -> v1, v1 -> N
- 만약 v1과 v2가 1과 N이면 1 -> N

이 3가지 경우 중 최단 거리를 출력하면 된다. 단, 구한 최단 거리가 MAX값보다 크면 -1을 출력해야한다. 

간선 수가 최대 20만, 가중치가 1000이니 최대값은 2억이고, 최단 거리가 2억 이상이면 -1을 출력하면 된다.

<br>

### 언어별 풀이 요약

| 언어   | 메모리   | 실행 시간(ms) | 시간복잡도   | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고            |
| ------ | -------- | ------------- | ------------ | ---------- | --------- | --------- | -------------------- |
| Python |          |               |              |            |           |           |                      |
| Java   | 69064 KB | 640 ms        | O(6 * ElogN) | O(N)       | 40분      | 2         | :white_large_square: |
| Kotlin |          |               |              |            |           |           |                      |

<br>

### 예외(테스트) 케이스

```
```
