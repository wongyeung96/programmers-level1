# programmers
programmers algorism study
def solution(n):
    answer = []
    #n을 10으로 나눈 나머지를 answer에 차례로 집어넣는다.
    while n >0:
        answer.append(n%10)
        #n은 10으로 나눈 몫으로 바꿔준다.
        n = n//10
    return answer
