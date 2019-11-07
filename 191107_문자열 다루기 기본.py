# programmers
programmers algorism study
def solution(s):
    import re
    a = []
	#만약 len(s)가 4나 6이면 len(s)와 len(a)를 비교한다.
    if len(s) ==4:
		#re.findall('[0-9]',s)는 문자열 s에서 숫자만 찾아서 출력해준다. 
        a = re.findall('[0-9]',s)
        return len(s) == len(a)
    elif len(s) ==6:
        a = re.findall('[0-9]',s)
        return len(s) == len(a)
	#len(s)가 4또는 6이 아니면 False값을 출력한다.
    else:
        return False
		
#이 풀이말고!
a = 'a123'
b = '1234'
a.isdigit()
#결과값 : False
b.isdigit()
#결과값 : True

#isdigit() 함수는 문자열에 숫자만 있으면 True 숫자이외의 값이 있으면 False를 출력
