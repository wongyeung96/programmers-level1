# programmers
programmers algorism study
def solution(n):
    answer =''
    #i가 홀수면 수를 짝수면 박을 출력한다.
    for i in range(1,n+1):
        if i%2 == 1:
            answer += '수'
        elif i%2 ==0:
            answer += '박'
    return answer
