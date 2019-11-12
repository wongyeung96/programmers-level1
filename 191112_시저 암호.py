# programmers
programmers algorism study
def solution(s,n):
    answer = ''
    alp = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    for i in range(0,len(s)):
    #만약 s[i]값이 대문자면 alp를 대문자로 변환하라
        if s[i].isupper() ==True:
            alp = alp.upper()
            num = alp.index(s[i])
            answer += alp[num+n]
    #만약 s[i]값이 소문자면 alp를 소문자로 변환하라
        elif s[i].islower() == True:
            alp = alp.lower()
                #s[i]문자가 alp에서 어디 위치인지 출력
            num = alp.index(s[i])
            answer += alp[num+n]
    #만약 공백이라면 공백을 answer에 집어넣어라
        elif s[i] == ' ':
            answer += ' '
    return answer
