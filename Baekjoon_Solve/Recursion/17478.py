# 재귀함수가 뭔가요?(17478번)
########################################################################################################
    # 문제: https://www.acmicpc.net/problem/17478
    # 재귀
    # 재귀 호출 종료 조건에 도달했을 때, 답변을 하면 된다.
    # 처음에 "을 잘못 찍어서 틀렸고, 그 다음에는 .을 잘못 찍어서 틀렸었다.
########################################################################################################
import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

N = int(input())

def recur(k):
    print('____' * k + '"재귀함수가 뭔가요?"')
    if k == N:
        print('____' * k + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print('____' * k + '라고 답변하였지.')
        return
    print('____' * k + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print('____' * k + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print('____' * k + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    recur(k+1)
    print('____' * k + '라고 답변하였지.')

print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
recur(0)