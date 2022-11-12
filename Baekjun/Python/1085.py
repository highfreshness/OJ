x, y, w, h = map(int, input().split())

x_axis = min(abs(x - 0), abs(x - w))
y_axis = min(abs(y - 0), abs(y - h))

print(min(x_axis, y_axis))


'''
이전 내 풀이
x, y, w, h = map(int, input().split())
result = []

result.append(x)
result.append(y)
result.append(h-y)
result.append(w-x)

print(min(result))
'''