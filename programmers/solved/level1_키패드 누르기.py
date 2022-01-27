def solution(numbers, hand):
    l_point =''
    r_point =''
    answer = ''
    keypad =  { 1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), '*':(3,0), 0:(3,1), '#':(3,2)} 
    
    for n in numbers:
        if n in [1,4,7,'*']:
            answer += 'L'
            l_point = n
        elif n in [3,6,9,'#']:
            answer += 'R'
            r_point = n
        else :
            l_range = abs(keypad[n][0] - keypad[l_point][0]) + abs(keypad[n][1] - keypad[l_point][1])
            r_range = abs(keypad[n][0] - keypad[r_point][0]) + abs(keypad[n][1] - keypad[r_point][1])
            if l_range > r_range:
                answer += 'R'
                r_point = n
            elif l_range < r_range:
                answer += 'L'
                l_point = n
            else :
                answer += hand[0].upper()
                if hand[0].upper() == 'L':
                    l_point = n
                else :
                    r_point = n
            
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = 'right'
print(solution(numbers, hand))

