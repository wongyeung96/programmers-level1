# programmers
programmers algorism study
def solution(num):
    answer = 0
    while num > 1:
        if num%2 == 0 and answer<501: #짝수면
            num = num/2
            answer = answer+1
        elif num%2 ==1 and answer<501: #홀수면
            num =(num*3)+1
            answer = answer+1
            #answer값이 500초과면 answer값 -1
        elif answer > 500:
            num = 0
            answer = -1
    return answer
