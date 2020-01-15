# programmers
programmers algorism study
def solution(x,n):
    answer = []
    for i in range(n):
        answer = answer + [x*(i+1)]
    return answer
    
    #answer에 차례대로 x*1,x*2 ... x*n의 값을 집어넣어준 후 출력한다. 
