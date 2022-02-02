n = int(input())

# 학생 이름과 성적을 dict로 수집
student_info = {}
for i in range(n):
    name, score = input().split()
    student_info[name] = int(score)

# dict value 기준으로 내림차순 정렬
student_info = sorted(student_info.items(), key=lambda x: x[1])

# 정렬된 dict에서 key 값만 출력
for n, s in student_info:
    print(n, end=" ")
