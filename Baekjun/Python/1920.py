import sys

INPUT = sys.stdin.readline
n = int(INPUT())
n_list = set(list(map(int, INPUT().split())))
m = int(INPUT())
m_list = list(map(int, INPUT().split()))

for x in m_list:
    if x in n_list:
        print(1)
    else:
        print(0)
