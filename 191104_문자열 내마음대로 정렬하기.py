# programmers
programmers algorism study
def solution(strings,n):
    plus =[]
    answer = []
    for i in strings:
        a = i[n] + i
        plus.append(a)
    plus.sort()
    for j in plus:
        answer.append(j[1:])
    return answer
