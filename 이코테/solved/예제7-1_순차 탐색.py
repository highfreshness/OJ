def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1


print('생성할 원소 갯수와 찾을 문자열 띄어쓰기 구분으로 입력하세요. ex) 3 선도')
input_data = input().split()
n = input_data[0]
target = input_data[1]

print('위의 생성할 원소의 갯수만큼 데이터를 띄어쓰기 구분으로 입력해주세요. ex)선도 라이언')
array = input().split()
print(sequential_search(n, target, array))
