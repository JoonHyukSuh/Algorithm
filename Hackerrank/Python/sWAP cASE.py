def swap_case(s):
    output = ''
    for i in s:
        if i.isupper() == True:
            output += i.lower()
        else:
            output += i.upper()
    return output
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)