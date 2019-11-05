# programmers
programmers algorism study

def solution(s):
    #1) 대문자와 소문자를 같게 하기 위해 모든 문자 소문자로 변경
    s = s.lower()
    
    #2) answer 값을 기본값 True로 지정
    answer = True
    
    #3) 만약 'p'의 count와 'y'의 count 값이 안같으면 answer 값 False로 지정
    if s.count('p') != s.count('y'):
        answer = False
    
    #4) answer  
    return answer
