limit = int(input())
str = ''

for x in range(limit):
    str += (limit-(x+1)) * ' '
    str += (x+1) * '*'
    print(str)
    str = ''
