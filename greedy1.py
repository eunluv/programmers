
n = 3
lost = [3]
reserve = [1]

def solution(n, lost, reserve):
    answer = 0
    stu_dic = {0:0}
    #stu_dic 초기화, 학생들은 처음엔 전부 체육복을 가지고 있었다.
    for i in range(1,n+1):
        stu_dic[i] = 1
    #여분의 체육복을 가지고 있던 학생들
    for i in reserve:
        stu_dic[i]+=1
    #체육복을 도난 당한 학생들
    for i in lost:
        stu_dic[i]-=1
    #여분의 체육복을 가지고 있는 학생들이 빌려 줄 수 있는지 확인
    for i in range(1,n+1):
        if i==1:
            if stu_dic[i]==0 and stu_dic[i+1] > 1:
                stu_dic[i]+=1
                stu_dic[i+1]-=1
        elif i==n:
            if stu_dic[i]==0 and stu_dic[i-1] > 1:
                stu_dic[i]+=1
                stu_dic[i-1]-=1
        else:
            if stu_dic[i]==0 and stu_dic[i-1] > 1:
                stu_dic[i]+=1
                stu_dic[i-1]-=1
            if stu_dic[i]==0 and stu_dic[i+1] > 1:
                stu_dic[i]+=1
                stu_dic[i+1]-=1    

    for i in range(1,n+1):
        if stu_dic[i]>=1:
            answer+=1
    return answer

print(solution(n,lost,reserve))