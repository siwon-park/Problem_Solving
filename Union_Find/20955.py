# 민서의 응급 수술(20955번)
######################################################################################
    # 문제: https://www.acmicpc.net/problem/20955
    # 분리집합, 트리
    # 처음에 문제를 잘못 읽어서 부모노드의 개수-1을 출력하면 끝인줄 알았다.
    # 그런데 문제를 잘 읽어보니, 연결하는 연산과 끊는 연산이 있다고 나와있었다
    # 그렇다면 사이클을 만드는 경우가 주어진다는 말이니까 부모를 비교했을 때, 아직 연결하지 않았는데도 부모가 같으면
    # 사이클이니 해당 경우에 대해 연결을 끊는 연산을 1번 한 것으로 쳐서 총 연산에 += 1을 해준다
    # 그리고 총 연산에 부모노드의 개수-1개를 더 해주면 된다. 이것은 서로 연결하는 연산이다.
    # 4번 시도한 끝에 풀었는데, 3번째 시도에서는 분명히 맞는데 왜 틀린거지 하고 봤더니
    # 나는 처음에 pn == 0이면 총 연산 횟수에 1을 더 해줘야한다고 생각했다. 지금 보니 왜 그렇게 생각했는지 모르겠지만,
    # pn == 0이라는 말은 모든 노드의 부모가 같다는 의미인데, 하지만 이미 이것을 연결하는 과정에서
    # 만약 사이클이 발생했다면 끊는 연산을 했을 것이고, 그게 아니라 사이클 없이 그냥 쭉 연결됬다면 어차피 총 연산은 0이므로
    # 현재의 총 연산수를 그대로 출력해도 되는 것이었다.
######################################################################################
import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
cnt = 0
for _ in range(M):
    u, v = map(int, input().split())
    if find(u) != find(v):
        union(u, v)
    else:
        cnt += 1 # 연결을 끊는 횟수

for i in range(1, N + 1): # 부모 노드를 최신화시키기 위해 모든 노드에 대해 find함수 호출
    find(i)

pn = len(set(parent[1:])) - 1
cnt += pn

print(cnt)
