s = input()

temp = s
answer = 0
n_dict = {'zero':0, 'one':1, 'two':2,'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9 }

for item in n_dict.items():
    temp = temp.replace(item[0], str(item[1]))
answer = int(temp)

print(answer)

