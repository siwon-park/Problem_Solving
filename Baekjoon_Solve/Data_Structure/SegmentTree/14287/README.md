## [플3] 회사 문화 3 (14287번)

https://www.acmicpc.net/problem/14287

### 문제 유형

자료 구조, 트리, 세그먼트 트리, 깊이 우선 탐색

<br>

### 어려웠던 점 / 문제의 핵심

발상이 특이한 재미있는 문제이다.

부모에서 자식으로 값이 내려가는 것이 아니라 자식에서 부모로 값이 역방향으로 올라간다.

따라서 5번 노드에 w1을, 2번 노드에 w2를 변경하면 1번 노드에 있는 값은 w1 + w2여야 한다.



![image](https://github.com/siwon-park/Problem_Solving/assets/93081720/0167ef96-61db-459e-919e-f09c0d24d837)

![image](https://github.com/siwon-park/Problem_Solving/assets/93081720/8e8f3824-33f4-4b81-b972-343763a324ba)

그렇다면 lazy값이나 w값을 과연 어떻게 누적 및 전달해야 하는가에 대한 의문이 남는다.

단순히 구간에 모두 w값을 업데이트하게 되면 부하-상사 관계에 있지 않은 노드를 판별하기가 쉽지 않다. (사실상 불가능)

이 아이디어는 `구간 합의 결과를 저장한 세그먼트 트리`를 통해 해결할 수 있다.

일단, lazy 배열을 통해 구간의 합(또는 값)을 빠르게 변경하는 로직이 필요한 것은 부인할 수 없다.

x번 노드가 칭찬을 받으면 구간 [x, x]에 대해서만 w값을 업데이트한다. 그렇게 되면 구간 [1, x]의 합은 w값이 업데이트된 값으로 적용이 된다.

위의 예시로 들면 5번 노드에 w1을 업데이트 하면, 그것을 부모 노드를 계속 찾아서 업데이트 시키지 말고 5번 노드에 그대로 w1의 값만 누적한다. 이렇게 한 다음, 1번 노드에 누적된 값을 호출하고자 할 때는 구간 [1, 5]의 합을 출력하면 된다.

어차피 5번 노드에 값을 업데이트 하면 실제로는 1번 노드도 업데이트 되는 것인데 직접적으로 1번 노드에 값을 전달하는 것이 아니라, 5번 노드에 값을 계속 누적하다가 구간 [1, 5]의 합을 출력하면 마치 1번 노드에만 쌓인 값을 계산할 수 있게 되는 것이다.

이는 아래 그림과 같다.

5번 노드에 값 w1을 업데이트 하면 1번 노드에도 업데이트 되는데, 이는 구간 [1, 5]의 합과 같다

![image](https://github.com/siwon-park/Problem_Solving/assets/93081720/966fa671-2d1e-4e5e-9a91-82605735f8c6)

마찬가지로, 2번 노드에 값 w2를 업데이트 하면 1번 노드에도 w2의 값이 누적되어 w1 + w2가 되는데, 이는 결국 구간 [1, 5]의 합과 같다.

![image](https://github.com/siwon-park/Problem_Solving/assets/93081720/e82c07e3-424a-484a-9448-85768f102ecf)

즉, 구간 합의 결과를 저장하고 있는 세그먼트 트리를 통해서 구간 [x, x]에 w 값을 업데이트한 다음에,

자식이 받은 w값을 반영한 구간 합의 결과를 부모가 가지고 있으면 되는 것이다.

<br>

### 언어별 풀이 요약

| 언어   | 메모리   | 실행 시간(ms) | 시간복잡도 | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고          |
| ------ | -------- | ------------- | ---------- | ---------- | --------- | --------- | ------------------ |
| Python |          |               |            |            |           |           |                    |
| Java   | 86868 KB | 920 ms        | O(MlogN)   | O(N * 4)   | 80분 +    | 4         | :white_check_mark: |
| Kotlin |          |               |            |            |           |           |                    |

<br>

### 예외(테스트) 케이스

```
```
