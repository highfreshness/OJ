# 0부터 9까지의 숫자 중 일부가 들어있는 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.


def solution(numbers):
    answer = -1
    n = [x for x in range(10)]
    answer = sum(list(set(n) - set(numbers)))
    return answer


numbers = [1, 2, 3, 4, 6, 7, 8, 0]
print(solution(numbers))
