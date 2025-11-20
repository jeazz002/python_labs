s = input()
s1  = s[1:len(s)]
flag = True
if 5 <= len(s) <= 15 and s[0] == '@' and s.isalnum == True:
    print('Correct')
else:
    print('Incorrect')