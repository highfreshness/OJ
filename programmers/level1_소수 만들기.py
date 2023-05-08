from itertools import combinations


def solution(nums):
    answer = 0
    for x in combinations(nums, 3):  # nums 내 원소를 3가지씩 조합해 튜플형태로 반환한다.(중복X)
        check_prime = sum(x)
        for i in range(2, check_prime - 1):
            if check_prime % i == 0:
                break
        else:
            answer += 1

    return answer


nums = [1, 2, 3, 4]
print(solution(nums))
