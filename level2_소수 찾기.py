from math import sqrt
from itertools import permutations


def is_prime_number(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    nums = [x for x in numbers]  # str인 numbers를 리스트 형태로 변환
    prime = []

    # num의 요소를 이용해 가질 수 있는 모든 수를 구한 후 중복 제거
    for i in range(1, len(nums) + 1):
        prime += list(permutations(nums, i))  # i의 차이로 생성된 리스트를 concatenation
        # 생성된 문자열을 정수로 변경하면 '011' => 11 로 변경
        new_prime = [int("".join(x)) for x in prime]

    for x in new_prime:
        if x > 1:  # 0, 1 은 소수 판별에 사용하지 않기 때문에 1보다 큰 수 일 때만 소수 판별 실행
            if is_prime_number(int(x)):
                answer += 1
    return answer


add = "011"
print(solution(add))
