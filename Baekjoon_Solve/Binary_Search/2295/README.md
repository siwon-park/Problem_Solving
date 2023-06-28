## [골4] 세 수의 합 (2295번)

https://www.acmicpc.net/problem/2295

### 문제 유형

자료 구조, 이분 탐색, 해시 맵, 밋 인 더 미들

<br>

### 어려웠던 점 / 문제의 핵심

이분 탐색으로도 문제를 풀 수 있고, 투 포인터로도 문제를 풀 수 있다.

#### 이분 탐색 풀이

4중 for문을 통해 해결하고자 한다면 `O(N ^ 4)`의 시간이 걸린다.

3중 for문을 통해 세 수의 합을 구하고 이분 탐색으로 세 수의 합을 찾는다면 `O(N ^ 3 * logN)`이 걸린다.

2중 for문을 통해 두 수의 합을 구하고 이분 탐색으로 남은 두 수의 합을 찾는다면(`two[i] + a[k] = a[l]`이니 `two에서 a[l] - a[k]`를 찾음) `O(N ^ 2 * logN)`의 시간이 걸린다.

#### 투 포인터 풀이

2중 for문으로 두 수를 고른다. 단 이 때 고른 두 수의 인덱스를 `i`, `j`라고 할 때 `i <= j`를 만족해야 한다.

그리고 `left`라는 인덱스를 두고 `i <= left`를 만족시킨다. (왼쪽 포인터)

그 다음 `right`라는 인덱스를 두고 끝에서 부터 출발시키되, `i <= right`를 역시 만족시켜야 한다.

- 만약 `i + j + left < right`라면 `right`의 인덱스를 감소
- 만약 `i + j + left > right`라면 `left`의 인덱스를 감소
- `i + j + left == right`라면 값을 찾은 것임
- `i`와 `j`는 for구문을 통해 인덱스를 큰 쪽에서 작은 쪽으로 감소시켜 나가니 따로 감소시킬 필요 없다.

<br>

### 언어별 풀이 요약

| 언어   | 메모리   | 실행 시간(ms) | 시간복잡도      | 공간복잡도 | 풀이 시간 | 시도 횟수 | 해설 참고          |
| ------ | -------- | ------------- | --------------- | ---------- | --------- | --------- | ------------------ |
| Python |          |               |                 |            |           |           |                    |
| Java   | 71016 KB | 1040 ms       | O(N ^ 2 * logN) | O(N ^ 2)   | 40분      | 1         | :white_check_mark: |
| Kotlin |          |               |                 |            |           |           |                    |

<br>

### 예외(테스트) 케이스

```
```
