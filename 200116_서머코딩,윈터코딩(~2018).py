# programmers
programmers algorism study

def solution(d,budget):
    answer = 0
    #d가 [1,3,2,5,4]일 때 오름차순 정렬 후 a에 저장.
    a = sorted(d)
    for i in a:
        if i <= budget:
            budget = budget-i
            answer += 1
    return answer
