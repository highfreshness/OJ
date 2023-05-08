def solution(s):
    answer = ''
    check = ''
    keypad = [
        ["0"],
        [".","Q","Z"],
        ["A","B","C"],
        ["D","E","F"],
        ["G","H","I"],
        ["J","K","L"],
        ["M","N","O"],
        ["P","R","S"],
        ["T","U","V"],
        ["W","X","Y"] 
    ]
    for idx, x in enumerate(s):
        if len(check) == 0 and x != "0":
            check += x
        else:
            if idx == len(s)-1:
                check += x
                answer += keypad[int(x)][len(check)-1]
            else:    
                if s[idx] == s[idx+1]:
                    check += x
                elif x == "0": 
                    continue
                else:
                    check += x
                    answer += keypad[int(x)][len(check)-1]
                    check = ''
            

    return answer
print(solution("44335550555666"))