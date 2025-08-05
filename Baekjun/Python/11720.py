"""
풀이:
    1. 첫번째 줄의 입력이 필요 없는 것으로 예상
    2. 리스트를 이용해 공백 없는 문자열 저장
    3. 각 문자열을 정수로 변환 후 합산하고 출력
시간복잡도: O(N)
변수:
    N : 문자열의 길이
    numbers : 공백 없는 문자열을 저장 할 리스트
"""

import sys

input = sys.stdin.readline # 굳이 대량의 인풋을 받을 것 같은 문제는 아닌 것으로 보임

N = int(input())
numbers = list(input().strip())
print(sum(map(int, numbers)))
