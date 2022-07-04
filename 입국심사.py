n = 6
times = [7, 10]
answer = 0

all_time = []
max_time = max(times) * n//len(times)

for i in times:
    count = n//len(times)
    while count * i <= max_time:
        all_time.append(count*i)
        count+=1
all_time.sort()
answer = all_time[len(times)-1]
print(answer)