# programmers
programmers algorism study
def solution(N,stages):
    answer =[]
    sort = []
    a =len(stages)
    s =0
    for i in range(1,N+1):
        if i in stages:
            a = a-s              #실패율 분모값 : 스테이지에 도달한 플레이어 수
            s = stages.count(i)  #실패율 분자값 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어수
            answer += [s/a]      #실패율
            sort += [s/a]
        else:             #클리어하지 못한 사람이 없는 단계는 실패율을 0으로 지정.
            answer += [0]
            sort += [0]
    sort.sort(reverse=True)
    for i in range(N):
        for j in range(N):
            if answer[i] == sort[j]:
                sort[j] = i+1
                answer[i] = i+1
    return sort
