## [골3] Strahler 순서 (9470번)

https://www.acmicpc.net/problem/9470

### 문제 유형

위상 정렬, 그래프 이론, 그래프 탐색

<br>

### 어려웠던 점 / 문제의 핵심

진입차수가 0이 되었을 때, strahler 순서의 최댓값이 총 몇 번 들어왔는지 체크하여

- 1번 들어왔다면 들어온 strahler 순서의 최댓값을 넣고,
- 2번 이상 들어왔다면 이제까지 들어온 strahler 순서의 최댓값 + 1을 넣는다.

최종적으로는 M번 노드의 strahler 순서를 출력하면 된다.

<br>

### 언어별 풀이 요약

| 언어   | 메모리   | 실행 시간(ms) | 시간복잡도 | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고            |
| ------ | -------- | ------------- | ---------- | ---------- | --------- | --------- | -------------------- |
| Python |          |               |            |            |           |           |                      |
| Java   | 16040 KB | 148 ms        | O(TM)      | O(M)       | 40분      | 1         | :white_large_square: |
| Kotlin |          |               |            |            |           |           |                      |

<br>

### 예외(테스트) 케이스

```
```
