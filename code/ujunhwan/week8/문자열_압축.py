def solution(string):
    answer = len(string)
    length = len(string)
    for num in range(1, length+1):
        cnt = 0
        cand = 0
        prev = string[0:num]
        last_idx = 0
        for i in range(0, length, num):
            last_idx = i
            if prev == string[i:i+num]:
                cnt += 1
            elif cnt >= 2:
                if cnt < 10:
                    cand += (1+num)
                elif cnt < 100:
                    cand += (2+num)
                elif cnt < 1000:
                    cand += (3+num)
                else:
                    cand += (4+num)
                prev = string[i:i+num]
                cnt = 1
            else:
                prev = string[i:i+num]
                cand += num
                cnt = 1
                
        if cnt >= 2:
            if cnt < 10:
                cand += (1+num)
            elif cnt < 100:
                cand += (2+num)
            elif cnt < 1000:
                cand += (3+num)
            else:
                cand += (4+num)
        else:
            cand += (length - last_idx)
        
        if answer > cand:
            answer = cand
        
    return answer