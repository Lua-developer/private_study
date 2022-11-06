a, b, n = map(int, input().split())
# 몫 부분
modules = a // b
# 소수 부분 구하기
result = (a / b) - modules
result = int(result * pow(10, n))
print(result % 10)