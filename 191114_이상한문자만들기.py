# programmers
programmers algorism study
def solution(s):
    #문자열 단어당 홀수인지 짝수인지 위치 파악 위해 count = 0 지정
    count = 0
    answer =''
    #공백이면 count=0으로 돌아오고 공백이 아니고 count가 짝수(각 단어당 짝수위치)이면 대문자출력, 홀수이면 소문자출력
    for i in range(0,len(s)):
        if (count%2 == 0) & (s[i] != ' '):
            answer+=s[i].upper()
            count += 1
        elif (count%2 == 1)&(s[i] != ' '):
            answer+=s[i].lower()
            count += 1
        #공백일 때는 answer에 공백 추가
        elif s[i] == ' ':
            answer += ' '
            count = 0
    return answer
