input_coin = int(input())
answer = 0

# # / - 나누기,  // - 몫,  % - 나머지
# answer += coin // 500
# answer += (coin % 500) // 100
# answer += ((coin % 500) % 100) // 50
# answer += (((coin % 500) % 100) % 50) // 10
# print(int(answer))

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    answer += input_coin // coin
    input_coin = input_coin % coin
    
print(answer)