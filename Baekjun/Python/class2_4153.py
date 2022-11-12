side = []
triangle = []

while(True):
    side = list(map(int, input().split()))

    if side[0] * side[1] * side[2] == 0:
        break
    else :
        triangle.append(sorted(side, reverse=False))
        
for x in triangle:
    a, b, c = x
    if (a**2 + b**2) == c**2:
        print('right')
    else : 
        print('wrong')