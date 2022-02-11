# Memoization = Cashing, 한번 구한 값을 저장해두고 필요할 떄 마다 꺼내 쓴다.

# 답을 저장해 둘 리스트
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    else :
        d[x] = fibo(x-1) + fibo(x-2)
        return d[x]
    
print(fibo(99))