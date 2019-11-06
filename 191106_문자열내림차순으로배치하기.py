# programmers
programmers algorism study
def solution(s):
    answer = ''
    
    #sorted는 문자열 정렬, reverse =  True는 내림차순.
    a=sorted(s,reverse = True)
    
    #a는 리스트 형식이므로 다시 문자열로 만들어준다.
    for i in a:
        answer = answer +i
    return answer
