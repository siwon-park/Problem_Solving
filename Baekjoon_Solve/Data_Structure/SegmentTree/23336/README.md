## [플5] A Sorting Problem (23336번)

https://www.acmicpc.net/problem/23336

### 문제 유형

자료 구조, 세그먼트 트리

<br>

### 어려웠던 점 / 문제의 핵심

문제를 해석하면 아래와 같다.

배열 p가 있는데, p[1], p[2], p[3], ..., p[n]에서 p[x]와 p[y]의 차이의 절댓값이 1일 때만 이 둘의 위치를 교환할 수 있다고 할 때, 배열 p를 오름차순 정렬하기 위해 필요한 최소 교환 횟수를 구하는 문제이다.

이 문제를 얼핏보면 두 요소의 차이 절댓값이 반드시 1일 때만 교환이 가능하다는 조건 때문에 다른 유형이라고 착각할 수도 있지만 결국에는 버블 정렬 혹은 선분 교차 문제와 동일한 유형이다.

왜냐하면 어차피 최종적으로는 오름차순 정렬이 되어야 하기 때문에 그렇다. 특정 순간에는 한 요소의 최적 위치까지 이동시키는데 드는 비용이 더 작을 수도 있겠지만 결국 교환 횟수는 버블정렬의 교환 횟수와 같을 수밖에 없다.

<br>

### 언어별 풀이 요약

| 언어   | 메모리   | 실행 시간(ms) | 시간복잡도 | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고            |
| ------ | -------- | ------------- | ---------- | ---------- | --------- | --------- | -------------------- |
| Python |          |               |            |            |           |           |                      |
| Java   | 50204 KB | 792 ms        | O(NlogN)   | O(N)       | 30분      | 1         | :white_large_square: |
| Kotlin |          |               |            |            |           |           |                      |

<br>

### 예외(테스트) 케이스

```
5
5 1 3 2 4
# ans: 5
```
