# 734 893

list_a = input().split()
list_a = [int(x[::-1]) for x in list_a]
print(max(list_a))
