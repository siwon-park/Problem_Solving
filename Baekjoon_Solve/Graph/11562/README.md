## [골3] 백양로 브레이크 (11562번)

https://www.acmicpc.net/problem/11562

### 문제 유형

그래프 이론, 플로이드 워셜

<br>

### 어려웠던 점 / 문제의 핵심

플로이드 워셜을 통해서 `s`에서 `e`까지 가는데 일방 통행인 길을 양방향 길로 바꿔야 하는 최소 횟수를 찾는 문제이다.

#### 시도 1

일방 통행은 비용 1, 양방향 통행은 비용 0으로 두고 `s`에서 `e`까지 갈 수 있으면 `0`을 출력하고,  `s`에서 `e`까지 갈 수 없으면 `e`에서 `s`까지 가는데 드는 비용을 출력했다.

왜냐하면 `a → b`로 갈 수 없다면 `b → a`로 일방 통행은 가능하기 때문이라고 생각했다.

그러나 이 풀이는 반례가 존재한다.

![image](https://github.com/siwon-park/Problem_Solving/assets/93081720/be9a1639-82b5-4ab8-b65c-16ec78335d18)

이와 같이 `A → C`도 불가능하고 `C → A`도 불가능한 경우가 존재하기 때문이다.

#### 올바른 접근법

` a → b`로 가는 단방향 길이 존재한다면 따로 이차원의 배열 상에 기록을 해둔다.

특정 위치에서 다른 위치로 갈 수 있는 경로가 존재한다면 그 경로를 사용하는 비용은 모두 0으로 가정한다.

그리고 플로이드 워셜로 모든 위치까지의 비용을 계산하는데,

만약 `i → k`로 갈 수 없는데 역방향으로는 일방 통행이 존재할 경우, 해당 비용을 1로 계산한다.

또한 `k → j`로 갈 수 없는데 역방향으로 일방 통행이 존재할 경우, 해당 비용을 1로 계산한다.

```java
int cost1 = graph[i][k];
int cost2 = graph[k][j];
// i -> k가 갈 수 없는데 역방향이 일방 통행이면 양방향으로 바꿈
if (graph[i][k] == MAX && oneWay[k][i] == 1) {
    cost1 = 1;
}
// k -> j가 갈 수 없는데 역방향이 일방 통행이면 양방향으로 바꿈
if (graph[k][j] == MAX && oneWay[j][k] == 1) {
    cost2 = 1;
}
graph[i][j] = Math.min(graph[i][j], cost1 + cost2);
```

이렇게 해서 플로이드 워셜을 통해 계산을 하게 되면 `s`에서 `e`까지 가는데 필요한 일방 통행을 양방향으로 바꾸는 최소 횟수를 계산할 수 있다.

<br>

### 언어별 풀이 요약

| 언어   | 메모리   | 실행 시간(ms) | 시간복잡도 | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고            |
| ------ | -------- | ------------- | ---------- | ---------- | --------- | --------- | -------------------- |
| Python |          |               |            |            |           |           |                      |
| Java   | 33320 KB | 496 ms        | O(N ^ 3)   | O(N ^ 2)   | 60분      | 3         | :white_large_square: |
| Kotlin |          |               |            |            |           |           |                      |

<br>

### 예외(테스트) 케이스

```
```
