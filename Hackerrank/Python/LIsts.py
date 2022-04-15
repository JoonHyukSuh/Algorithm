if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        command, *num = input().split()
        num_list = list(map(int,num))
        
        if command == 'insert':
            arr.insert(num_list[0],num_list[1])
        elif command == 'append':
            arr.append(num_list[0])
        elif command == 'remove':
            try:
                arr.remove(num_list[0])
            except:
                pass
        elif command == 'print':
            print(arr)
        elif command == 'sort':
            arr.sort()
        elif command == 'pop':
            arr.pop()
        elif command == 'reverse':
            arr = arr[::-1]