# programmers
programmers algorism study
def solution(x):
    answer = 0
    y = str(x)
    for i in range(len(y)):
        answer = answer + int(y[i])
    return x%answer ==0
    
    #x숫자를 문자열로 바꾼후 for문을 통해 자릿수의 값들을 더한 후
    #x에서 더한 값 answer을 나누었을 때 나누어 떨어지면 True, 나누어 떨어지지 않으면 False
