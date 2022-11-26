n = int(input())

t_list = [int(input()) for _ in range(n)]
t_list.sort()
[print(x, end="\n")for x in t_list]