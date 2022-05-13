def solution(records):
    cand = []
    answer = []
    
    dic = dict()
    dic["Enter"] = "님이 들어왔습니다."
    dic["Leave"] = "님이 나갔습니다."
    
    for record in records:
        s = record.split()
        if len(s) > 2:
            dic[s[1]] = s[2]
        cand.append([s[0], s[1]])
    
    for c in cand:
        if c[0] == "Change":
            continue
        answer.append(dic[c[1]] + dic[c[0]])
        
    return answer