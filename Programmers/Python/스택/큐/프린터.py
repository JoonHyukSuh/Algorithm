def solution(priorities, location):
    answer = 0
    while True:
        maxnum = max(priorities)
        for i in range(len(priorities)):
            if maxnum == priorities[i]:
                answer += 1
                priorities[i] = 0 
                maxnum = max(priorities)
                if i == location:
                    return answer