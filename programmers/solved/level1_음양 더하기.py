def solution(absolutes, signs):
    answer = sum([(-x if y == False else x) for x, y in zip(absolutes, signs)])
    return answer
