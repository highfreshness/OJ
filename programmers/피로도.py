from collections import deque

def solution(k, dungeons):
    max = 0
    queue  = deque(dungeons)
    
    for _ in range(len(dungeons)):
        temp = queue.popleft()
        queue.append(temp)
        cnt = 0
        k_temp = k
        for x in queue:
            if x[0] <= k_temp:
                cnt += 1
                k_temp -= x[1]
        if max < cnt:
            max = cnt
    return max
print(solution(80, [[80,20],[50,40],[30,10]]))