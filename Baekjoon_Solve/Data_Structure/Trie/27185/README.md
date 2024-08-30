## [골1] The Tree (27185번)

https://www.acmicpc.net/problem/27185

### 문제 유형

자료 구조, 트리, 트라이, 느리게 갱신되는 세그먼트 트리

<br>

### 어려웠던 점 / 문제의 핵심

문제를 해석하면 다음과 같다.

무한 이진 트리에 대해서 다음과 같은 문제를 풀어야 한다.

쿼리의 수 q와 모듈러 연산을 위한 상수 c가 주어진다.

q개의 쿼리는 다음과 같다.

- t가 1인 경우 해당 노드의 색을 x로 칠한다.
  - 이 때 왼쪽 자식 L은 (x + 1) % c, 오른쪽 자식 R은 (x - 1 + c) % c로 칠한다.
- t가 2인 경우 해당 노드의 현재 색을 출력한다.
- 각 쿼리 별로 루트 노드에서 현재 노드까지에 대한 정보가 주어진다. 이를 통해 현재 노드 u를 파악해야 하며, L은 왼쪽, R은 오른쪽으로 이동한다는 의미이다.

#### 어려웠던 점

문제를 보면 느리게 갱신되는 세그먼트 트리로 풀 수 있을 것 같다. (실제로도 느리게 갱신되는 세그먼트 트리 유형이라고 되어 있다.)

그래서 전위 순회를 통해 노드의 방문 순서를 구하고 구간을 정해서 업데이트 하는 방식으로 구현해보았는데 답이 잘 나오지 않았다.

구현에 실수가 있었을 수도 있지만 주어지는 모든 경로의 길이 합이 5 x 10^5 이하라고 해서 노드 수를 확정 지을 수 없었기 때문이다.

#### 문제의 핵심

트라이(Trie) + 구현으로 풀었다. (트라이 보다는 구현에 더 가까운 것 같다.)

왼쪽 자식과 오른쪽 자식만 있는 트라이를 구현하되, 느리게 갱신되는 세그먼트 트리를 구할 때처럼 자식을 찾아가면서 lazy값이 -1이 아니면 전파하는 방식으로 구현하였다.

주어지는 모든 경로 길이의 합이 5 x 10^5을 넘지 않기 때문에 O(N)인 선형 시간으로도 풀 수 있다. 

<br>

### 언어별 풀이 요약

| 언어   | 메모리    | 실행 시간(ms) | 시간복잡도 | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고            |
| ------ | --------- | ------------- | ---------- | ---------- | --------- | --------- | -------------------- |
| Python |           |               |            |            |           |           |                      |
| Java   | 132148 KB | 668 ms        | O(N)       | O(N)       | 80분      | 1         | :white_large_square: |
| Kotlin |           |               |            |            |           |           |                      |

<br>

### 예외(테스트) 케이스

```
```
