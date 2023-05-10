## [골4] 탈출 (16397번)

https://www.acmicpc.net/problem/16397

### 문제 유형

그래프 이론, 그래프 탐색, BFS

<br>

### 어려웠던 점 / 문제의 핵심

문제에서 주어진 내용을 그대로 구현하기만 하면 되는 BFS문제이다.

가장 먼저 방문한 숫자가 최단 거리를 보장하기 때문에 딱히 신경 쓸만한 예외는 없다.

B버튼을 눌렀을 때, 숫자의 2배가 아니라 숫자의 2배를 한 다음에 가장 높은 자리수의 숫자를 1 감소시켜야 한다.

이를 구현하기 위해 if-else 구문을 남발했는데, math 라이브러리를 활용해 밑이 10인 로그와 올림을 활용해서 조건문 없이 해결할 수도 있었다.

<br>

### 언어별 풀이 요약

| 언어   | 메모리   | 실행 시간(ms) | 시간복잡도 | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고            |
| ------ | -------- | ------------- | ---------- | ---------- | --------- | --------- | -------------------- |
| Python | 34252 KB | 128 ms        | O(N)       | O(N)       | 30분      | 1         | :white_large_square: |
| Java   |          |               |            |            |           |           |                      |
| Kotlin |          |               |            |            |           |           |                      |

<br>

### 예외(테스트) 케이스

```
```
