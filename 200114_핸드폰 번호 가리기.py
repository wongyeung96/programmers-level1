# programmers
programmers algorism study
def solution(phone_number):
    answer =''
    for i in range(len(phone_number)):
        if i < len(phone_number)-4:
            answer+='*'
        else:
            answer+=phone_number[i]
    return answer
    
    #전화번호의 4자리를 제외한 나머지 글자수일때는 *를 집어넣고 나머지는 phone_number에 있는 숫자를 집어넣는다.
    
 #다른 풀이
 def solution(phone_number):
    return "*"*(len(phone_number)-4) + s[-4:]
