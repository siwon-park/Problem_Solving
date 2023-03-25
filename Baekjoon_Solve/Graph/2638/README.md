## [골3] 치즈 (2638번)

https://www.acmicpc.net/problem/2638

### 문제 유형

구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 시뮬레이션, 깊이 우선 탐색

<br>

### 어려웠던 점 / 문제의 핵심

이중으로 while문을 돌면서, `현재 공기큐에서 bfs 너비 우선 탐색을 했을 때, 다음 위치가 공기이면 현재 공기큐에 삽입하고, 만약 다음 위치가 치즈이면서 두 번째 방문일 경우에는 다음 공기 큐에 삽입한다.` 

현재 공기큐가 비었으면 다음 공기큐를 현재 공기큐로 하고 이를 치즈가 다 녹을 때까지 반복한다. 만약 다음 공기큐가 비었으면 치즈가 전부 녹은 것이니 break하고 시간을 return 한다.

<br>

### 언어별 풀이 요약

| 언어   | 메모리   | 실행 시간(ms) | 시간복잡도 | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고            |
| ------ | -------- | ------------- | ---------- | ---------- | --------- | --------- | -------------------- |
| Python |          |               |            |            |           |           |                      |
| Java   | 15424 KB | 172 ms        | O(NM)      | O(N^2)     | 35분      | 1         | :white_large_square: |
| Kotlin |          |               |            |            |           |           |                      |

<br>

### 예외(테스트) 케이스

```
```
