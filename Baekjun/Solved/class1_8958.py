# 5
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX

cnt = int(input())
input_list = []

result = 0
extra_point = 0
result_list = []

for x in range(cnt):
    input_list.append(input())


for attr in input_list:
    for j in attr:
        if j == 'O':
            extra_point += 1
            result += extra_point
        else:
            extra_point = 0
    result_list.append(result)
    extra_point = 0
    result = 0

for a in result_list:
    print(a)
