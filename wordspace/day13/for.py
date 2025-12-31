#%% for test
for i in range(0, 10, 1):
    print("%d한동석" %(i+1))
    
for i in range(10, 0, -1):
    print("%d한동석" %i)
    
#0부터 1씩 증가시키는 for문을 작성한다
#단, 10~1까지 출력한다.
for i in range(0, 10, 1):
    print(10 - i)

# n + 0 = 10
# 1. n = 10
# 2. 10 - 0

#%% for test
# =============================================================================
# 고수 : 반복문 시작값을 무조건 0으로 고정
# 1~100까지 출력
# 100~1까지 출력
# 1~100까지 중 짝수만 출력
# A~F 까지 출력
# A~F 까지 중 C 제외하고 출력
# aBcDeFgHiJkLmNoPqRsTuVwXyZ 출력
# =============================================================================

#1번 문제
for i in range(0, 100, 1):
    print(i+1)
    
#2번 문제
for i in range(100, 0, -1):
    print(i)
for i in range(0, 100, 1):
    print(100 - i)

#3번 문제    
for i in range(0, 100, 1):
    if i%2 == 0:
        print(i + 2)
for i in range(0, 50, 1): 
    print((i + 1)*2)