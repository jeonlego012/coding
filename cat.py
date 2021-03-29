s, n = input().strip().split(' ')
n = int(n)

leftStr = ''
centerStr = ''
rightStr = ''

leftStr += s

for i in range(int((n-len(s))/2)) :
    centerStr += ' '
centerStr += s

for i in range(n-len(s)) :
    rightStr += ' '
rightStr += s

print(leftStr)
print(centerStr)
print(rightStr)

########################################
s, n = input().strip().split(' ')
n = int(n)
print(s.ljust(n))
print(s.center(n))
print(s.rjust(n))