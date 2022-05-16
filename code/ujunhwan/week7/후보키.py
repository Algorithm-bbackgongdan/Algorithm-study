from itertools import combinations

def solution(relation):
    C = len(relation[0])
    R = len(relation)
    
    def check(comb):
        dic = dict()
        for i in range(R):
            s = ""
            for j in comb:
                s += (relation[i][j] + "//")
            if s not in dic:
                dic[s] = 0
            dic[s] += 1
        return max(dic.values()) == 1
    
    # uniqueness
    uniq = []
    for level in range(1, C+1):
        comb = list(combinations(range(C), level))
        for c in comb:
            #print(list(c))
            if check(c):
                uniq.append(list(c))
    
    # print(uniq)
    
    # minimality
    answer = []
    
    def exam(lst):
        for i in range(len(lst)):
            for c in combinations(lst, i):
                if list(c) in answer:
                    return False
        return True
            
    for comb in uniq:
        if exam(comb):
            # 모든 부분집합을 검사 ?
            answer.append(comb)
            
    #print(answer)
    return len(answer)