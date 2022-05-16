from itertools import combinations

def solution(relation):
    answer = 0
    
    # column의 개수가 key의 원소의 개수가 될 수 있다.
    N = len(relation[0])
    M = len(relation)
    
    # checklist - 이미 key가 되어버린 것은 다른 곳에 참여 불가능
    checklist = [0 for i in range(N)]
    
    # 원소의 개수가 1, 2, 3 순으로 증가시키면서 key가 될 수 있는 값들 확인
    for elementNum in range(1,N+1):
        hash_table = {}
        key_list = []
        # print(hash_table)
        for rel in relation:
            c = list(combinations(rel, elementNum))
            index_num = list(combinations(range(N), elementNum))
            for idx, group in enumerate(c):
                value = ''.join(group)
                key = ''.join(''.join(map(str, index_num[idx])))
                if key not in key_list:
                    key_list.append(key)
                
                # hash_table 만들기
                try:
                    if hash_table[key]:
                        if value not in hash_table[key]:
                            hash_table[key].append(value)
                except KeyError:
                    hash_table[key] = [value]
                    
        # hash_table에서 key해 해당하는 배열 길이가 relation개수이면 걔는 key.
        for key in key_list:
            if len(hash_table[key]) == M:
                templist = list(key)
                count = 0
                for t in templist:
                    if checklist[int(t)] == 1:
                        break
                    else:
                        count+=1
                if count == len(templist):
                    answer += 1
                
                for t in templist:
                    if count == len(templist):
                        checklist[int(t)] = 1
                    
        # print(answer)
        # print(key_list)
        # print(hash_table)
        # print(checklist)
    return answer