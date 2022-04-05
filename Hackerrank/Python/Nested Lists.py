if __name__ == '__main__':
    student_list = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_list.append([name,score])
        score_list.append(score)
        
    student_list.sort(key = lambda x: x[0])
    second_lowest = sorted(set(score_list))[1]
    for name, score in student_list:
        if score == second_lowest:
            print(name)
