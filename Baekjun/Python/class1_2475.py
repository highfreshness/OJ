key_value = list(map(int, input().split()))
square_sum = []

for x in key_value:
    square_sum.append(x**2)

print(sum(square_sum) % 10)
