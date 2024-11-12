## [골5] 시간을 돌리고 싶어 (32347번)

[https://www.acmicpc.net/problem/32347]()

### 문제 유형

이분 탐색, 매개 변수 탐색

<br>

### 어려웠던 점 / 문제의 핵심

타임머신 사용 횟수를 K이하로 하고, 과거로 가는 일수 T를 최소화했을 때의 T값을 찾는 문제이다.

N과 K가 최대 20만이기 때문에 단순 반복문을 사용하면 시간초과가 난다.

따라서 탐색 범위가 매우 크기 때문에 이분 탐색을 통해서 T를 찾아야 한다.

그런데 타임머신을 사용하려면 사용 시점에 충전 여부가 1이어야 한다. 그렇기 때문에 만약에 과거로 갔는데 그 시점에 충전 중이지 않으면 과거에서 시간을 보내서 미래로 이동한 다음 다시 타임머신을 타고 과거로 가야 한다.

일일히 하나씩 미래 일자에 대해 체크하면 이 역시 시간초과가 발생하게 된다.

따라서 과거 시점으로 왔을 때 충전 여부가 0이면 충전 여부가 1인 가장 가까운 미래에 대한 정보를 바로 알 수 있어야 한다.

입력으로 받은 충전 여부 배열을 역순하여 시점 i를 기준으로 충전 여부가 1인 가장 가까운 미래를 새로운 배열에 기록하여 사용하면 된다.

<br>

### 언어별 풀이 요약

| 언어   | 메모리   | 실행 시간(ms) | 시간복잡도 | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고            |
| ------ | -------- | ------------- | ---------- | ---------- | --------- | --------- | -------------------- |
| Python |          |               |            |            |           |           |                      |
| Java   | 31792 KB | 308 ms        | O(NlogK)   | O(N)       | 30분      | 1         | :white_large_square: |
| Kotlin |          |               |            |            |           |           |                      |

<br>

### 예외(테스트) 케이스

```
```
