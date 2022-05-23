def solution(s):
    s = s.split('},')
    for i, p in enumerate(s):
        s[i] = p.split(',')
    for i, p in enumerate(s):
        for ii, f in enumerate(p):
            p[ii] = f.replace('{', '').replace('}', '')
            
    answer = []
    
    s.sort(key=lambda x:len(x))
    dic = dict()
                
    for p in s:
        for f in p:
            cnt = dict()
            if f not in dic:
                dic[f] = 0
            if f not in cnt:
                cnt[f] = 0
            cnt[f] += 1
            if cnt[f] > dic[f]:
                dic[f] += 1
                answer.append(int(f))
            
    print(dic)
    return answer