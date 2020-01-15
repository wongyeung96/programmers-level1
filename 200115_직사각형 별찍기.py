# programmers
programmers algorism study
#map 함수로 a와 b에 숫자 대입
#입력할 때 5 3 이런식으로 입력하면 된다.
a,b = map(int,input().strip().split(' '))
for i in range(b):
	print('*'*a)
