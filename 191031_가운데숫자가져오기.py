# programmers
programmers algorism study
def solution(s):
    a = len(s)
    answer = ''
    if a%2 == 1:
        answer = s[((a+1)//2)-1]
    else:
        answer = s[(a//2)-1:(a//2)+1]
    return answer
