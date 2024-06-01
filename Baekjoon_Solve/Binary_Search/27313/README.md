## [골4] 효율적인 애니메이션 감상 (27313번)

https://www.acmicpc.net/problem/27313

### 문제 유형

매개 변수 탐색, 그리디, 정렬

<br>

### 어려웠던 점 / 문제의 핵심

애니메이션 감상 시간을 정렬하여, 감상 가능한 애니메이션 개수를 매개변수로 하여 M이하의 시간 동안 최대 몇 개까지 감상 가능한지 찾는다.

우선 애니메이션 감상 시간을 배열에 넣고 정렬한다. 만약 가장 앞에 있는 감상 시간이 M보다 크면 1개도 감상하지 못하기 때문에 0을 반환한다. 아니라면, `mid개부터 역순으로 K개까지 시청`하면서 구간의 제일 큰 감상시간만큼 누적 합산한다.

최댓값이 가장 많이 있는 구간을 더 많이 그리디하게 선택하는 것이 누적 시간이 항상 더 작게 나오기 때문에 이득이다.

mid개 이하로 볼 수 있는 총 시간이 M이하면 볼 수 있는 개수를 늘려보고, 아니면 줄여서 탐색을 계속한다.

<br>

### 언어별 풀이 요약

| 언어   | 메모리   | 실행 시간(ms) | 시간복잡도     | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고          |
| ------ | -------- | ------------- | -------------- | ---------- | --------- | --------- | ------------------ |
| Python |          |               |                |            |           |           |                    |
| Java   | 29820 KB | 460 ms        | O((N//K)*logN) | O(N)       | 70분      | 2         | :white_check_mark: |
| Kotlin |          |               |                |            |           |           |                    |

<br>

### 예외(테스트) 케이스

```
```
