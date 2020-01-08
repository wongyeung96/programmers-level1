# programmers
programmers algorism study
def solution(arr):
    #만약 arr의 리스트 길이가 1보다 길면 최솟값을 제거
    if len(arr)>1:
        arr.remove(min(arr))
    #만약 arr의 리스트 길이가 1이면 -1의 값만 출력
    else:
        arr=[-1]
    return(arr)
