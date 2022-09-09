# 당근 훔쳐 먹기(18234번)
##################################################################################
    # 문제: https://www.acmicpc.net/problem/18234
    # 그리디, 정렬
    # 이게 왜 골드3인지 모를 정도로 쉽다. 개인적인 체감 난이도는 실버 하위권인듯하다.
    # T일 동안 재배하지만, 토끼는 당근을 먹지 않고 넘어갈 수도 있으므로 T- N + 1일차 오후부터 영양제 증가량이 낮은 당근부터 먹으면 최상의 맛으로 당근을 즐길 수 있다 
    # 나는 역순으로 정렬해서 풀었다.
    # 주어지는 당근의 맛과 영양제 정보를 배열에 담아서 역순 정렬해주고,
    # 해당 당근의 초기값 + 영양제로 인한 맛 증가량 * (T - i - 1)일을 N번 반복하였다.
##################################################################################
import sys
input = sys.stdin.readline

N, T = map(int, input().split())
carrots = []
for _ in range(N):
    w, p = map(int, input().split())
    carrots.append((w, p))

carrots.sort(key=lambda x: (-x[1], -x[0]))

ans = 0
for i in range(N):
    ans += carrots[i][1] * (T - i - 1) + carrots[i][0]
print(ans)