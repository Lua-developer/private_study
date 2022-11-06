import copy

scores = []
rank = []
for _ in range(8) :
	inputs = int(input())
	scores.append(inputs)
# sort
copy_score = copy.deepcopy(scores)
scores.sort(reverse=True)
sum_score = sum(scores[:5])
for i in range(5) :
    for k in range(8) :
        if scores[i] == copy_score[k] :
            rank.append(k + 1)
rank.sort()
print(sum_score)
for r in rank :
    print(r, end=" ")