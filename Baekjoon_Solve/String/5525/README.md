## [실1] IOIOI

https://www.acmicpc.net/problem/5525

### 문제 유형

문자열

<br>

### 어려웠던 점 / 문제의 핵심

그냥 생각없이 풀면 `O(N^2)`의 시간 복잡도를 가지게 되어 TLE 판정을 받을 수 있음.

따라서 O(M)의 시간 복잡도로 풀어야함.

Pn에는 Pn-1이 2개 들었고, Pn-2이 3개, ... P1은 n개 있음.

즉, 문자열 S에서 Pn이 몇 개 들어있는지 확인하려면 P1이 연속으로 N개 나온 갯수를 세면 됨.

이 때, 가장 중요한 것이 s[i:i+2]가 "IOI"였다면 IOI가 연속적으로 이어지기 위해서는 Pn = IOIOI...이기 때문에

i+3의 위치가 아니라, i+2의 위치에서 시작해서 s[i+2:i+4]를 확인해야 한다.

<br>

### 언어별 풀이 요약

| 언어   | 메모리   | 실행 시간(ms) | 시간복잡도 | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고          |
| ------ | -------- | ------------- | ---------- | ---------- | --------- | --------- | ------------------ |
| Python |          |               |            |            |           |           |                    |
| Java   | 20040 KB | 276 ms        | O(M)       | O(1)       | 40분      | 1         | :white_check_mark: |
| Kotlin |          |               |            |            |           |           |                    |

<br>

### 예외(테스트) 케이스

```
```
