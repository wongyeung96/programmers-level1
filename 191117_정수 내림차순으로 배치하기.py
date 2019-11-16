# programmers
programmers algorism study
def solution(n):
    answer = []
    a =''
    #정수 n을 10으로 나눈 후 나머지를 str형으로바꾼후 answer에 추가한다.
    while n>0:
        answer.append(str(n%10))
        n = n//10
    # 다 만들어진 answer를 reverse = True로 내림차순으로 정렬.
    answer = sorted(answer,reverse = True)
    #list인 answer의 값들을 a =''안에 차례로 넣어준다.
    for i in answer:
        a += i
    # str형인 a를 int로 출력
    return int(a)
