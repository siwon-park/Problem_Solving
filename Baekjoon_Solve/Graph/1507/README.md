## [골2] 궁금한 민호 (1507번)

https://www.acmicpc.net/problem/1507

### 문제 유형

그래프 이론, 최단 경로, 플로이드-워셜

<br>

### 어려웠던 점 / 문제의 핵심

#### 러프한 풀이

우리가 갖고 있는 것은 이미 플로이드 워셜을 돌린 최단 경로 테이블이다.

이를 역으로 분해해서 연결 그래프를 찾아야 한다. `N <= 20`이기 때문에 `i → j`가 최소인 부분부터 시작해서 그래프 탐색으로 찾으면 플로이드-워셜을 돌리기 전의 연결 그래프를 찾을 수 있다. 이를 통해 정답을 구할 수도 있을 것이다.

#### 플로이드 워셜 풀이

그러나 플로이드-워셜로 푸는 방법도 있다. 아이디어가 재밌는데, `a → k → b == a → b`이면 `a → b 간선을 사용하지 않는다.`

그럼 여기서 들만한 반문은 `"최소 경로로 만들려면, a → b 간선만 살려야 하는 게 아닌가?"`이다.

이에 답을 하자면 `a → k, k → b, a → b` 이렇게 3개의 간선에서 1개를 삭제하는 것이니, 경로의 수를 감소하는 것은 맞다.

또한 `a → b만 남기고 나머지 2개를 삭제하는 것이 항상 올바르지 않을 수도 있다.` a → b의 관점만 보면 두 지점의 연결 경로만 남기는 것이 맞지만, 나머지 다른 노드들의 관점에서는 삭제되면 안 되는 연결 정보일 수도 있다.

k도 결국 1 ~ N이기 때문에 이런 방식으로 삭제하다보면 결국 남은 경로들이 최소 경로가 된다.

최종적으로 `a → b인 남은 경로들에 대해서 최단 경로 값들의 합`을 구하면 정답이다.

경로를 삭제할 때는 반드시 a, b, k 모두 달라야 한다. 왜냐하면 자기 자신에서 자기 자신으로 가는 경로는 0이기 때문에 잘못하면 자기 자신을 삭제해버릴 수도 있기 때문이다.

<br>

### 언어별 풀이 요약

| 언어   | 메모리   | 실행 시간(ms) | 시간복잡도 | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고          |
| ------ | -------- | ------------- | ---------- | ---------- | --------- | --------- | ------------------ |
| Python |          |               |            |            |           |           |                    |
| Java   | 14372 KB | 132 ms        | O(N^3)     | O(N^2)     | 70분      | 1         | :white_check_mark: |
| Kotlin |          |               |            |            |           |           |                    |

<br>

### 예외(테스트) 케이스

```
```
