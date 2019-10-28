# programmers
programmers algorism study
 def solution(n,lost,reserve):
        lost.sort()
        reserve.sort()
        set_lost = list(set(lost) - set(reserve))
        set_reserve = list(set(reserve) - set(lost))
        for i in set_reserve:
            if i-1 in set_lost:
                set_lost.remove(i-1)
            elif i+1 in set_lost:
                set_lost.remove(i+1)
        return n-(len(set_lost))
