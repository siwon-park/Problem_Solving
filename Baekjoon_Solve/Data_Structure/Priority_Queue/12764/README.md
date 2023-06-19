## [골3] 싸지방에 간 준하 (12764번)

https://www.acmicpc.net/problem/12764

### 문제 유형

구현, 자료 구조, 시뮬레이션, 우선순위 큐

<br>

### 어려웠던 점 / 문제의 핵심

풀이 자체는 자바 풀이가 더 직관적임. 그러나 속도는 파이썬이 더 빠르다.

#### 파이썬 풀이

시작 시간이 빠른 순으로 정렬한다.

끝나는 시간이 빠른 우선 순위 큐와 CPU 번호가 가장 빠른 우선 순위 큐를 구성한다.

- CPU 번호에 대한 우선 순위 큐는 빠른 번호를 가진 CPU를 이용하기 위함임
  - 단순히 끝나는 시간이 빠른 우선 순위 큐의 크기를 이용해서 CPU 번호를 할당하면 더 빠른 CPU를 쓸 수 있음에도 불구하고 할당하지 못하는 경우가 있기 때문임

우선 순위 큐가 비어 있으면 1번 컴퓨터가 사용 가능하므로 우선 순위 큐에 삽입한다.

우선 순위 큐가 비어 있지 않으면, 현재 시간(=현재 우선 순위 큐에 들어오려는 작업의 시작 시간)이 우선 순위 큐의 제일 위에 있는 시간 보다 큰지 작은지 확인한다.

현재 시간이 작으면 아직 우선 순위 큐에서 나갈 요소가 없다는 의미이므로 원래 요소를 다시 집어 넣는다.

현재 시간이 더 크다면 큰 동안 우선 순위 큐에서 계속해서 뺀다.

그 후 현재 진입하려는 요소를 집어 넣는데, 사용이 끝난 CPU 중 가장 빠른 번호의 CPU가 있으면 해당 CPU 번호를 집어 넣고, 없다면 현재 우선 순위 큐의 크기를 CPU 번호로 집어 넣는다.

그 후 우선 순위 큐의 크기를 1 증가시키고, 최대 사용 CPU의 개수를 갱신한다.

남은 우선 순위 큐와 CPU 사용 빈도에 대한 작업을 처리해주면 된다.

#### 자바 풀이

시작 시간이 빠른 순으로 우선 순위 큐에 집어 넣는다.

우선 순위 큐에서 요소를 뽑으면서 매번 컴퓨터의 최대 개수인 N번 순회한다. (break가 있어 최대 N번 순회하지는 않음)

만약 i번째 cpu 배열에 기록된 끝나는 시간이 현재 시작 시간보다 작으면 cpu[i]에 현재 우선 순위 큐에서 나온 요소의 끝나는 시간을 기록하고 i번째 컴퓨터의 사용 빈도 수를 1 증가시킨다. 그 후 break하여 순회를 종료하고 다시 우선 순위 큐에서 계속해서 요소를 뽑는다.

(i번째 cpu 배열에 기록된 끝나는 시간이 현재 시작 시간보다 크면 그 컴퓨터는 계속해서 사용 중이라는 의미이다.)

<br>

### 언어별 풀이 요약

자바 풀이의 경우 N ^ 2이지만 break 구문 때문에 절대 N ^ 2으로 갈 수 없어 N보다 작은 수인 K를 곱한 값으로 간주하였음. 파이썬의 경우 2NlogN보다는 작은 시간이 걸림.

| 언어   | 메모리   | 실행 시간(ms) | 시간복잡도       | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고            |
| ------ | -------- | ------------- | ---------------- | ---------- | --------- | --------- | -------------------- |
| Python | 54040 KB | 644 ms        | O(NlogN + KlogN) | O(N)       | 40분      | 2         | :white_large_square: |
| Java   | 42588 KB | 1044 ms       | O(NlogN + NK)    | O(N)       | 60분      | 2         | :white_large_square: |
| Kotlin |          |               |                  |            |           |           |                      |

<br>

### 예외(테스트) 케이스

```
```
