# programmers
programmers algorism study
# 내가 푼것(66줄,, ㅎㅎ)
def solution(n, arr1, arr2):
    answer = []
    a3 = []
    for i in range(n):
        for j in range(n-1,-1,-1):
            if arr1[i] % 2 == 0: #arr1의 원소 값이 짝수이면
                if arr1[i]>=2**j:
                    arr1[i]=arr1[i]-2**j
                    answer += [1]
                elif arr1[i] < 2**j:
                    answer += [0]
            if arr1[i] % 2 != 0: #arr1의 원소 값이 홀수이면
                if arr1[i]>=2**j:
                    arr1[i]=arr1[i]-2**j
                    answer += [1]
                elif arr1[i] < 2**j:
                    answer += [0]
                elif j==0:
                    answer += [1]
    for i in range(n):
        for j in range(n-1,-1,-1):
            if arr2[i] % 2 == 0: #arr2의 원소 값이 짝수이면
                if arr2[i]>=2**j:
                    arr2[i]=arr2[i]-2**j
                    answer += [1]
                elif arr2[i] < 2**j:
                    answer += [0]
            if arr2[i] % 2 != 0: #arr2의 원소 값이 홀수이면
                if arr2[i]>=2**j:
                    arr2[i]=arr2[i]-2**j
                    answer += [1]
                elif arr2[i] < 2**j:
                    answer += [0]
                elif j==0:
                    answer += [1]
    a1 = answer[0:len(answer)//2] #배열 1
    a2 = answer[len(answer)//2:len(answer)] #배열 2
    for i in range(0,len(a1)):
        if a1[i] == 1:
            a1[i] = '#'
        else:
            a1[i] = ' '
    for i in range(0,len(a2)):
        if a2[i] == 1:
            a2[i] = '#'
        else:
            a2[i] = ' '
    for i in range(0,len(a1)):
        if a1[i] == a2[i]:
            a3 = a3+[a1[i]]
        if a1[i] != a2[i]:
            a3 = a3+["#"]
    count=0
    b=''
    c=[]
    a4 = a3
    for i in range(0,len(a3)+n):
        if count == n:
            count = 0
            c = c+[b]
            b=''
        else:
            b = b+a4[0]
            del a4[0]
            count += 1
    return c
    
    solution(5,[9,20,28,18,11],[30,1,21,17,28])
    solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10])
    
    #쉬운 풀이법
    def solution(n, arr1, arr2):
    answer = []
    #zip으로 하면 i와 j에 (9,30),(20,1),(28,21),,,순으로 입력.
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:]) #bin은 이진수 만드는 함수. bin(9|30)을 하면 9와 30에 1의 합집합의 값을 나타낸다.
                                #그리고  bin(i|j)만 하게되면 ex)0b11111이므로 0b를 없애기 위해 [2:]을 추가한다.
        a12=a12.rjust(n,'0')    #rjust는 n의 수만큼 오른쪽부터 n자리로 만드는데 빈 곳은 0으로 대체한다.
        a12=a12.replace('1','#') #replace는 글씨를 바꾸는 함수. 1을 '#'으로 바꾼다.
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
