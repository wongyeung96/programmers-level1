# programmers
programmers algorism study
def solution(strings,n):
    #1) 1차 출력물 plus와 2차 출력물 answer로 나눔
    plus =[]
    answer = []
    
    #2) n번째 문자를 i의 문자 맨앞에 붙여주고 오름차순 정렬.
    for i in strings:
        a = i[n] + i
        plus.append(a)
    plus.sort()
    
    #3) 오름차순 정렬 한 plus에서 필요없는 부분인 0부분을 뺀 나머지 값만 answer에 저장. 
    for j in plus:
        answer.append(j[1:])
    
    #4) 
    return answer
