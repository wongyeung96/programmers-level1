# programmers
programmers algorism study

def solution(n,m):
    answer = []
    c = []
    d = []
    e = []
    #만약 m이 n보다 크다면 
    if n < m:
        #c에 m의 약수를 저장
        for i in range(1,m+1):
            if m%i ==0:
                c.append(i)
        #d에 m의 약수 중에서 n의 약수인 것을 저장
        for j in c:
            if n%j ==0:
                d.append(j)
        #그 중 제일 큰 최대공약수를 answer에 저장
        answer.append(max(d))
        #큰수m부터 m*n중 공배수를 찾아서 e에 저장
        for z in range(m,(m*n)+1):
            if z%n==0 and z%m==0:
                e.append(z)
        #그 중 제일 작은 최소공배수를 answer에 저장
        answer.append(min(e))
    #만약 n이 m보다 크다면
    if n > m:
        #c에 n의 약수를 저장
        for i in range(1,n+1):
            if n%i ==0:
                c.append(i)
        #d에 n의 약수 중에서 m의 약수인 것을 저장        
        for j in c:
            if m%j ==0:
                d.append(j)
        #그 중 제일 큰 최대공약수를 answer에 저장
        answer.append(max(d))
        #큰수n부터 m*n중 공배수를 찾아서 e에 저장
        for z in range(n,(m*n)+1):
            if z%m==0 and z%n==0:
                e.append(z)
        #그 중 제일 작은 최소공배수를 answer에 저장        
        answer.append(min(e))
    return answer
