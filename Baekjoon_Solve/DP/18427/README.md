## [골4] 함께 블록 쌓기 (18427번)

https://www.acmicpc.net/problem/18427

### 문제 유형

DP, 배낭문제

<br>

### 어려웠던 점 / 문제의 핵심

`dp[i][j]`를 `i개의 학생으로 높이 j를 만들 수 있는 경우의 수`라고 정의한다.

그러면 `dp[i][0] = 1`이다. i번 모두 선택하지 않으면 되기 때문.

그리고 `j >= h`이면 `dp[i][j] += dp[i - 1][j - h]`이다. i번째 학생의 블럭 중 하나를 선택 하는 경우의 수를 누적 계산하는 것이다.

마지막으로 `dp[i][j] += dp[i - 1][j]`이다. i번째 학생의 블럭을 선택하지 않고 j의 높이를 만들 수 있는 경우의 수를 누적하기 위함이다.

<br>

### 언어별 풀이 요약

| 언어   | 메모리   | 실행 시간(ms) | 시간복잡도 | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고          |
| ------ | -------- | ------------- | ---------- | ---------- | --------- | --------- | ------------------ |
| Python |          |               |            |            |           |           |                    |
| Java   | 15284 KB | 172 ms        | O(KMN)     | O(KN)      | 30분      | 2         | :white_check_mark: |
| Kotlin |          |               |            |            |           |           |                    |

<br>

### 예외(테스트) 케이스

```
```
