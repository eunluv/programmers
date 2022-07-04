N = 5
number = 5

def solution(N, number):
    num = {1:[N]}
    cnt = 1 #N이 사용된 개수
    if number == N:
        return cnt
    while cnt <= 8:
        cnt+=1
        num[cnt]=[int(str(N)*cnt)]
        for i in range(cnt-1,cnt//2-1,-1):
            j = cnt - i
            for p1 in num[i]:
                for p2 in num[j]:
                    num[cnt].append(p1+p2)
                    num[cnt].append(p1-p2)
                    num[cnt].append(p1*p2)
                    if p2 != 0:
                        num[cnt].append(p1//p2)        
        if number in num[cnt]:
            return cnt
    if cnt > 8:
        return -1

print(solution(N, number))



        # for i in num[cnt-1]:
        #        n_num = int(str(N)*cnt)
        #    if n_num == number:
        #        break
        #    num[cnt].append(n_num)
        #    n_num = i + N
        #    if n_num == number:
        #        break
        #    num[cnt].append(n_num)
        #    n_num = i - N
        #    if n_num == number:
        #        break
        #    num[cnt].append(n_num)
        #    n_num = i * N
        #    if n_num == number:
        #        break
        #    num[cnt].append(n_num)
        #    n_num = i // N
        #    if n_num == number:
        #        break
        #    num[cnt].append(n_num)
    
    #         if cnt == 2:
    #             for i in num[cnt-1]:            
    #             num[cnt].append(i+i)
    #             num[cnt].append(i-i)
    #             num[cnt].append(i*i)
    #             num[cnt].append(i//i)
    #     else:
    #         for i in range(cnt-1,cnt//2-1,-1):
    #             j = cnt - i
    #             for p1 in num[i]:
    #                 for p2 in num[j]:
    #                     num[cnt].append(p1+p2)
    #                     num[cnt].append(p1-p2)
    #                     num[cnt].append(p1*p2)
    #                     if p2 != 0:
    #                         num[cnt].append(p1//p2)        
    #     if number in num[cnt]:
    #         return cnt
    # if cnt > 8:
    #     return -1