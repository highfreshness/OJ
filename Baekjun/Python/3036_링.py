def GCD(x, y):
    while y:
        x, y = y, x % y
    return x


n = int(input())
num_list = list(map(int, input().split()))

for x in range(0, len(num_list) - 1):
    gcd = GCD(num_list[0], num_list[x + 1])
    print(f"{num_list[0]//gcd}/{num_list[x+1]//gcd}")
