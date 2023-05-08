# def solution(answers):
#     answer = []
#     answer_sheet = []
#     cnt = 1
#     score = 0
#     score_dict = {}
    
#     pattern = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
#     for p in pattern:
#         for j in p:
#             if len(answer_sheet) < len(answers):
#                 answer_sheet.append(j)
#             else :
#                 break
#         for x, y in zip(answer_sheet, answers):
#             if x == y:
#                 score += 1
#         score_dict[cnt] = score
#         answer_sheet = []
#         score = 0
#         cnt += 1
        
#     # score_dict = sorted(score_dict.items(), key=lambda item:item[1], reverse=True)
#     if max(score_dict.values()) * 3 == sum(score_dict.values()):
#         answer = [1,2,3]
#     elif max(score_dict.values()) * 2 == sum(score_dict.values()) - min(score_dict.values()):
#         del score_dict[min(score_dict.items())[0]]
#         answer.append((score_dict.keys()))
#     else :
#         answer.append(max(score_dict.items(), key=lambda x:x[1])[0])
#     return answer

# answer1 = [1,2,3,4,5]
# answer2 = [1,3,2,4,2]
# print(solution(answer2))

from itertools import cycle # 무한 반복을 위한 cycle

def solution(answers):
    test_taker = [  # 수포자 패턴 리스트
        cycle([1,2,3,4,5]), 
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5])]
    scores = [0,0,0] # 정답 리스트
    
    # n번째 문제 정답을 수포자1,2,3을 돌아가며 정답과 비교하고 맞으면 점수 리스트에 1점 추가
    for answer in answers:
        for i in range(3):
            if next(test_taker[i]) == answer: 
                scores[i] += 1
                
    # 최고 점수와 동일한 인덱스의 수포자를 리스트로 반환 
    return [i+1 for i in range(len(scores)) if scores[i] == max(scores)] 