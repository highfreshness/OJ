# def solution(lottos, win_nums):
#     answer = []
#     high_cnt = 0 # 최고점 등수
#     low_cnt = 0 # 최저점 등수
#     rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6} # 로또 당첨 등수

#     #최고점
#     for x in lottos:
#         if (x in win_nums) | (x == 0):
#             high_cnt += 1
#     answer.append(rank[high_cnt])

#     #최저점
#     for x in lottos:
#         if x in win_nums:
#             low_cnt += 1
#     answer.append(rank[low_cnt])

#     return answer


def solution(lottos, win_nums):
    answer = []
    rank = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6,
    }  # 로또 당첨 등수 dict, 모든 숫자가 안 맞아도 6등이기 떄문에 0도 같이 넣어줘야 한다.

    cnt_0 = lottos.count(0)  # lottos 안의 0 카운트
    cnt = len(
        set(lottos) & set(win_nums)
    )  # lottos 와 win_nums의 교집합 갯수를 확인하기 위해 set으로 변경 후 len 사용
    answer.append(rank[cnt + cnt_0])  # 최고점
    answer.append(rank[cnt])  # 최저점

    return answer
