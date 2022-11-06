import sys
n = int(sys.stdin.readline())
height_list = []
for i in range(n) :
    h = int(sys.stdin.readline())
    height_list.append(h)
count = 1
# 뒤집기
height_list.reverse()
# 제일 첫번째꺼
maximum = height_list[0]
for index in range(1, n) :
    if maximum < height_list[index] :
        maximum = height_list[index]
        count += 1
print(count)