# programmers
programmers algorism study
def solution(s):
    s = s.lower()
    answer = True
    if s.count('p') != s.count('y'):
        answer = False
    return answer
