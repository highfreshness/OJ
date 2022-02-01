arr_limit = int(input())

array = []
for i in range(arr_limit):
    array.append(input())

array.sort(reverse=True)

for i in array:
    print(i, end=" ")

