length = int(input())
score = list(map(int, input().split()))

new_score = []
max_score = max(score)

for x in score:
    new_score.append((x / max_score) * 100)

result = sum(new_score)/length
print(result)
