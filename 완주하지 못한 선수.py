# programmers
programmers algorism study

#나의 풀이
 def solution(participant,completion):
	answer = ""
	participant.sort()
	completion.sort()
	completion.insert(len(participant),"zzzzzzzzzzzzzzzzzzzzz")
	for i in range(0,len(participant)):
		if participant[i] != completion[i]:
		  answer = participant[i]
		  break
	return answer.lower()
	
