def solution(numbers, target):
    A = [0]
    for i in numbers:
        temp = []
        for j in A:
            temp.append(j+i)
            temp.append(j-i)
        A = temp
    print(temp)
    return temp.count(target)

print(solution([1, 1, 1, 1, 1], 3))