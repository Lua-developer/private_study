a, b, n = map(int, input().split())
# 몫 부분
modules = a // b
# 소수 부분 구하기
other = a / b
answer = int((other - modules) * pow(10, n))
answer = list(map(int, str(answer)))
print(answer[-1])