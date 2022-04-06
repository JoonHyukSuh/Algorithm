#1259 팰린드롬수 
while TRUE:
  word = input()
  palindrome = word[::-1]

  if word =='0':
    break

  if word == palindrome:
    print('yes')
  else:
    print('no')
 