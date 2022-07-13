from collections import deque 
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    cnt = 0
    while progresses:
        if progresses[0] + speeds[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        else:
            if cnt:
                answer.append(cnt)
                cnt = 0
            else:
                for i in range(len(progresses)):
                    progresses[i] += speeds[i]
    answer.append(cnt)
    return answer