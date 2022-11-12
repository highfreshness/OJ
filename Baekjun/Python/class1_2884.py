hour, minute = map(int, input().split())

if (minute - 45) < 0:
    minute = 60 + (minute - 45)
    if (hour - 1) < 0:
        hour = 24 + (hour - 1)
        print(f'{hour} {minute}')
    else:
        hour = hour - 1
        print(f'{hour} {minute}')
else:
    minute = minute - 45
    print(f'{hour} {minute}')
