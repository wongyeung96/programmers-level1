# programmers
programmers algorism study
def solution(n):
    answer = n
    #약수는 n/2보다 큰 값이 없으므로 범위를 (n/2)+1로 해준다.
    for i in range(1,int((n/2)+1)):
        if (n%i == 0): 
            answer += i 
    return answer
