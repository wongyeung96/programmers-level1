# programmers
programmers algorism study
def solution(s):
    answer =0
    #s의 자릿수를 문자열로 뽑아내 다시 int형으로 바꾼후 answer에 계속 더해준다.
    for i in str(s):
        answer += int(i)
    return(answer)
