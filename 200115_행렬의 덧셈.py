# programmers
programmers algorism study
def solution(a,b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = a[i][j]+b[i][j]
    return a
    
    #a행렬의 1행1열 = a행렬의 1행1열+b행렬의 1행1열
    #a행렬의 1행2열 = a행렬의 1행2열+b행렬의 1행2열 식으로 
    #a 행렬의 결과가 a와 b 행렬의 합으로 나타나도록 표현했다.
    
