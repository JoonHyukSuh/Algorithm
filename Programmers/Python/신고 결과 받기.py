from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    new_report = []
    users = defaultdict(list)
    prison = defaultdict(int)
    new_report = list(set(report))
    
    for i in new_report:
        a , b = i.split()
        users[a].append(b)
        prison[b] += 1
    for i in id_list:
        cnt = 0
        for user in users[i]:
            if prison[user] >= k:
                cnt += 1
        answer.append(cnt)
    return answer

