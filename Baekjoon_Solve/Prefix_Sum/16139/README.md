## [실1] 인간-컴퓨터 상호작용 (16139번)

https://www.acmicpc.net/problem/16139

### 문제 유형

누적 합

<br>

### 어려웠던 점 / 문제의 핵심

`arr[26][len(S)]`인 배열을 선언하고 주어지는 문자열에 대한 누적 합을 계산한 다음

주어지는 쿼리의 문자열의 아스키 코드 값 - 97에 해당하는 인덱스 번호와 구간 [l, r] 사이에 존재하는 해당 알파벳의 개수를 출력하면 된다.

python3로는 시간초과가 나서 pypy3로 제출하였다.

<br>

### 언어별 풀이 요약

| 언어   | 메모리    | 실행 시간(ms) | 시간복잡도 | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고            |
| ------ | --------- | ------------- | ---------- | ---------- | --------- | --------- | -------------------- |
| Python | 152980 KB | 344 ms        | O(N + Q)   | O(N)       | 30분      | 2         | :white_large_square: |
| Java   |           |               |            |            |           |           |                      |
| Kotlin |           |               |            |            |           |           |                      |

<br>

### 예외(테스트) 케이스

```
```
