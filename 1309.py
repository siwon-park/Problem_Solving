#동물원(1309번) 
########################################
    # 문제: https://www.acmicpc.net/problem/1309
    # 다이나믹 프로그래밍
    # 역시 다이나믹 프로그래밍은 아직까지 익숙치 않아서 계속 연습해야 할듯하다. 이번에도 고민하다가 힌트를 얻어서 풀었다.
    # 100ms 풀이와 256ms 풀이를 올린다.
########################################

# 100ms 풀이; # 점화식: dp[i]=(2*dp[i-1]+dp[i-2])%9901
N=int(input())
dp=[0]*(N+1)
dp[0],dp[1]=1,3
for i in range(2,N+1):
    dp[i]=(2*dp[i-1]+dp[i-2])%9901
print(dp[N])

#########################################

# 256ms 풀이
# 점화식 설명; dp[N][0]: 공백, dp[N][1]: 좌, dp[N][2]: 우라 함
# N     1  2  3  4   ...
# 공백  1  3  7  17  ...
# 좌    1  2  5  12  ...
# 우    1  2  5  12  ...
# 위 표에서 보듯이 (1) N의 마지막 칸이 공백이면 N-1일 때, 공백이든 좌, 우에 사자를 놓아도 다 가능하다 따라서 dp[N][공백]=dp[N-1][공백]+dp[N-1][좌]+dp[N-1][우]
# 마찬가지로 (2) N의 마지막 칸의 좌측에 사자를 위치 시키려면 N-1의 마지막 칸이 공백이었거나 우측에 사자가 있어야하므로 dp[N][좌]=dp[N-1][공백]+dp[N-1][우]
# (3) N의 마지막 칸의 우측에 사자를 위치 시키려면 N-1의 마지막 칸이 공백이었거나 좌측에 사자가 있어야하므로 dp[N-1][우]=dp[N-1][공백]+dp[N-1][좌] 이다.
# 두 풀이의 점화식은 사실상 같고 256ms 풀이의 점화식을 간단하게 한 것이 100ms의 점화식임
N=int(input())
dp=[[0,0,0,0] for i in range(N+1)]
dp[1]=[1,1,1,3]
for i in range(2,N+1):
    dp[i][0]=(dp[i-1][0]+dp[i-1][1]+dp[i-1][2])%9901
    dp[i][1]=(dp[i-1][0]+dp[i-1][2])%9901
    dp[i][2]=(dp[i-1][0]+dp[i-1][1])%9901
    dp[i][3]=(dp[i][0]+dp[i][1]+dp[i][2])%9901 # 마지막에 3개를 더했을 때도 더한 값이 9901을 넘으면 오버플로우가 생길 수 있으므로 %9901을 해줘야함
print(dp[N][3])
