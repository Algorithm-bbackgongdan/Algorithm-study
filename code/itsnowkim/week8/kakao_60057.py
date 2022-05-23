def solution(s):
    answer = len(s)
    result = []
    
    for i in range(1,len(s)+1):
        sentence = ''
        last = 0
        while last < len(s):
            cnt =1
            while s[last:last+i] == s[last+i:last+i+i]:
                cnt+=1
                last += i
            if cnt > 1:
                sentence = sentence + str(cnt)
            sentence = sentence + s[last:last+i]
            last = last + i
        result.append(len(sentence))
    
    
    return min(result)