def solution(array, commands):
    answer = []
    for i in commands:
        n_array = array[i[0]-1 : i[1]]
        n_array.sort()
        answer.append(n_array[i[2]-1])
    return answer