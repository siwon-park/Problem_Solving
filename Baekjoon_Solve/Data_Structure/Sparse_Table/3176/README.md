## [플4] 도로 네트워크 (3176번)

https://www.acmicpc.net/problem/3176

### 문제 유형

자료 구조, 트리, 최소 공통 조상, 희소 배열

<br>

### 어려웠던 점 / 문제의 핵심

희소 배열을 통해 `n`의 `2 ^ k`번째 부모를 알 수 있다.

마찬가지로 DP의 원리와 희소 배열을 통해 `n`의 `2 ^ k`번째 부모로 가는데 있는 가장 짧은 도로 길이, 가장 긴 도로 길이를 구할 수도 있다.

```java
minDist[n][k + 1] = Math.min(minDist[parent[n][k]][k], minDist[n][k]);
maxDist[n][k + 1] = Math.max(maxDist[parent[n][k]][k], maxDist[n][k]);
```

따라서 희소 배열을 활용하여 LCA를 구하면서 LCA에 이르기까지 드는 가장 짧은 길이, 가장 긴 길이를 구할 수 있다.

#### 실수했던 점

- `서로 다른` 두 자연수 D와 E가 주어진다 => 서로 같은 정점이면서 LCA일 경우 0, 0을 출력하기 위해서 예외처리를 하고 있었다.
- `n`의 `2 ^ k`번째 부모로 가는데 있는 가장 짧은 도로 길이, 가장 긴 도로 길이를 구하기 위해서는
  - `minDist[parent[n][k]][k]`과 `minDist[n][k + 1]`을 비교하는 것이 아니라 `minDist[n][k]`와 비교해야 한다.
  - 왜냐하면 말 그래도 `n`에서 `2 ^ k`번째 있는 부모까지 올라가는 길에 있는 도로의 경로 중에서 가장 짧은 혹은 가장 긴 도로의 길이를 구하는 것이기 때문에 `2 ^ k`번째 부모의 경로가 더 짧다면, ` 2 ^ (K + 1)`의 값도 `2 ^ K`의 값이어야 한다. (다이나믹 프로그래밍을 생각하면 된다.)

<br>

### 언어별 풀이 요약

| 언어   | 메모리    | 실행 시간(ms) | 시간복잡도 | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고          |
| ------ | --------- | ------------- | ---------- | ---------- | --------- | --------- | ------------------ |
| Python |           |               |            |            |           |           |                    |
| Java   | 116964 KB | 1468 ms       | O(MlogN)   | O(N)       | 180 분    | 6         | :white_check_mark: |
| Kotlin |           |               |            |            |           |           |                    |

<br>

### 예외(테스트) 케이스

```
```
