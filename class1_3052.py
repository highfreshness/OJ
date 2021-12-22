input_list = []

for x in range(10):
    input_list.append(int(input()) % 42)

set_list = set(input_list)
print(len(set_list))
