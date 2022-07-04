'''
progresses = [95,90,99,99,80,99]#[93, 30, 55]
speeds = [1,1,1,1,1,1]#[1, 30, 5]


def solution(progresses, speeds):
    day = list()
    answer = list()
    n = len(progresses)
    #작업 소요 기간 저장
    for i in range(n):
        if progresses[i]%speeds[i]==0:
            day.append((100 - progresses[i])//speeds[i])
        else:
            day.append(((100 - progresses[i])//speeds[i])+1)
    print(day)
    
print(solution(progresses, speeds))
'''

scoville = [1,2,3,9,10,12]
K = 7

def solution(scoville, K):
    answer = 0
    for i in scoville:
        scoville.sort()
        new = scoville[0] + (scoville[1]*2)
        if new < K:
            del scoville[0:1]
            scoville.append(new)
            answer += 1
        else:
            answer += 1
            break

    if scoville[-1]>= K:
        print(answer)
        return answer
    else:
        return -1
    

solution(scoville, K)
