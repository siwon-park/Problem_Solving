## [골4] 루머 (19538번)

https://www.acmicpc.net/problem/19538

### 문제 유형

그래프 이론, 그래프 탐색, BFS

<br>

### 어려웠던 점 / 문제의 핵심

위상정렬 로직과 유사한 너비 우선 탐색 문제이다.

다음 노드 `nxt`가 인접 노드들로부터 들은 루머의 수를 `nearBy[nxt]`라고 할 때, `nearBy[nxt]`가 연결된 인접 노드의 수(`graph[nxt].size()`)의 절반 이상이면 방문 체크를 하고 큐에 삽입한다.

큐에 삽입하는 시점에 루머를 믿게 되므로 해당 시간을 time 배열에 기록하면 된다.

<br>

### 언어별 풀이 요약

K는 양방향 연결 관계의 수

| 언어   | 메모리    | 실행 시간(ms) | 시간복잡도 | 공간복잡도   | 풀이 시간 | 시도 횟수 | 해설 참고            |
| ------ | --------- | ------------- | ---------- | ------------ | --------- | --------- | -------------------- |
| Python |           |               |            |              |           |           |                      |
| Java   | 235964 KB | 1060 ms       | O(M + K)   | O(M + N + K) | 40분      | 1         | :white_large_square: |
| Kotlin |           |               |            |              |           |           |                      |

<br>

### 예외(테스트) 케이스

```
```
