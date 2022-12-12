# 문어 숫자 (1864번)
##########################################################################################
    # 문제: https://www.acmicpc.net/problem/1864
    # 수학, 구현, 문자열
    # \에 대해서 문자열 자체를 표현하기 위해 \\로 쓸 줄 알면 쉽게 풀 수 있다.
##########################################################################################
import sys
input = sys.stdin.readline

num_dict = {"-": 0, "\\": 1, "(": 2, "@": 3, "?": 4, ">": 5, "&": 6, "%": 7, "/": -1}

while True:
    inp = input().rstrip()
    if inp == "#":
        break
    n = len(inp)
    ans = 0
    for i in range(n):
        ans += num_dict[inp[i]] * (8 ** (n - 1 - i))
    print(ans)