# 2초(8,000만) / 실버 5 / 슬라이딩 윈도우
import sys
input = sys.stdin.readline

# 변수 초기화
my_list = [0] * 4
check_var = 0

def myadd(char):
    global my_list, pass_check, check_var
    if char=='A':
        my_list[0] += 1
        if my_list[0] == pass_check[0]:
            check_var += 1
    elif char=='C':
        my_list[1] += 1
        if my_list[1] == pass_check[1]:
            check_var += 1
    elif char=="G":
        my_list[2] += 1
        if my_list[2] == pass_check[2]:
            check_var += 1
    elif char=="T":
        my_list[3] += 1
        if my_list[3] == pass_check[3]:
            check_var += 1
            
def myremove(char):
    global my_list, pass_check, check_var
    if char=='A':
        if my_list[0] == pass_check[0]:
            check_var -= 1
        my_list[0] -= 1
    elif char=='C':
        if my_list[1] == pass_check[1]:
            check_var -= 1
        my_list[1] -= 1
    elif char=="G":
        if my_list[2] == pass_check[2]:
            check_var -= 1
        my_list[2] -= 1
    elif char=="T":
        if my_list[3] == pass_check[3]:
            check_var -= 1
        my_list[3] -= 1
        
s, p = map(int, input().split())
answer = 0
A = list(input())
pass_check = list(map(int, input().split()))

for i in range(4):
    if pass_check[i] == 0:
        check_var += 1
        
for i in range(p):
    myadd(A[i])
    
if check_var == 4:
    answer += 1
    
for i in range(p, s):
    j = i - p
    myadd(A[i])
    myremove(A[j])
    if check_var == 4:
        answer += 1

print(answer)
    
    

