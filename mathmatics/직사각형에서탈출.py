x, y, w, h = map(int, input().split())
x_diff = abs(x - w)
y_diff = abs(y - h)
result = [x,y,x_diff,y_diff]
print(min(result))