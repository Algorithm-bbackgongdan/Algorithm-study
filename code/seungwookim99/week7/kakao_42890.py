from itertools import combinations

def is_unique(atts, relation):
    tmp = []
    for r in relation:
        row = tuple(r[i] for i in atts)
        tmp.append(row)
    
    return len(set(tmp)) == len(tmp)

def solution(relation):
    atts_num = len(relation[0])
    unique_atts = []
    
    for i in range(1,atts_num+1):
        for atts in combinations(range(atts_num), i):
            # 유일성 검사
            if not is_unique(atts, relation):
                continue
            # 최소성 검사
            for uni in unique_atts:
                if len(uni - set(atts)) == 0:
                    break
            else:
                unique_atts.append(set(atts))
                
    return len(unique_atts)