numbers = [4,1,2,1]
target = 4

answer = 0
n = len(numbers)
queue = [0]

for i in numbers:
    temp = []
    for j in queue:
        temp.append(j+i)
        temp.append(j-i)
    queue = temp

for q in queue:
    if q == target:
        answer += 1

print(answer)