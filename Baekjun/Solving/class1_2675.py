num = int(input())
list1 = []

for i in range(num):
    list1.append(input())

for j in list1:
    a, b = j.split()
    mul1 = [x*int(a) for x in b]
    print("".join(mul1))
