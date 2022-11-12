n, m = map(int, input().split())
card_list = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i+1, n):
        for x in range(j+1, n):
            if card_list[i] + card_list[j] + card_list[x] > m:
                continue
            else:
                result = max(result, card_list[i] + card_list[j] + card_list[x])
                
print(result)