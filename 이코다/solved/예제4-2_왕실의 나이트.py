""" ASCII코드표 에서 알파벳 소문자는 97~122의 10진수로 표기되기 된다. 따라서 a~h를 
    아스키 코드로 변호나 후 +1을 해주면 ... 1~8의 숫자형태로 변환이 가능하다
"""

point = input()
row = int(point[1])  # ex) a1 일 경우 1
column = int(ord(point[0]) - (ord("a"))) + 1
# 나이트가 있는 한 점에서 이동할 수 있는 경우의 수 8개를 좌표로 설정
steps = [(-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, -2), (-2, 1), (-2, -1)]
result = 0
# 입력된 row, column 기준으로 step의 결과를 확인
for step in steps:
    move_row = row + step[1]
    move_column = column + step[0]
    # row 나 column이 1 이상, 8 이하인 경우 카운트
    if move_row >= 1 and move_row <= 8 and move_column >= 1 and move_column <= 8:
        result += 1

print(result)
