x, y, w, h = map(int, input().split())
result = []

result.append(x)
result.append(y)
result.append(h-y)
result.append(w-x)

print(min(result))
