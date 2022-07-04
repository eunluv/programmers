participant = ["mislav", "stanko", "mislav","mislav", "ana"]
completion = ["stanko", "mislav", "mislav","mislav"]

'''
a = ord('a')
z = ord('z')

par_table = {'participant':len(participant)} #참가 인원해시 생성
com_table = {'completion':len(completion)} #완주 인원해시 생성

for i in range(a,z+1): #com_table 초기화('a'-'z')
    com_table[chr(i)]=[]

for i in participant: #par_table 초기화(이름)
    par_table[i]=False

for i in completion: #해시에 완주자 저장
    key = i[0]
    com_table[key].append(i)

for i in participant: #완주 못한 사람 찾기
    key = i[0]
    if i in com_table[key]:
        par_table[i]=not par_table[i]
        
    if (par_table[i]==False):
        answer = i

print(answer)
'''

par_table = dict();

for i in participant:
    if i not in par_table.keys():
        par_table[i] = 1
    else:
        par_table[i] += 1

print(par_table)

for i in completion:
    par_table[i] -= 1

for i in participant:
    if par_table[i] == 1:
        answer = i

print(answer)
    

