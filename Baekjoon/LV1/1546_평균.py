a = input()
b = input().split()
score_list = []
for i in b:
    score_list.append(int(i))
max_score = max(score_list)
new_score = []
for i in score_list:
    i = i / max_score*100
    new_score.append(float(i))

mean_score = round(sum(new_score) / int(a),2)
print(mean_score)