input_list = []
total = 1

for x in range(3):
    input_list.append(int(input()))
    total *= input_list[x]

total = str(total)

for i in range(10):
    print(total.count(str(i)))
