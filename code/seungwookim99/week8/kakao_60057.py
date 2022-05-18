def solution(s):
    answer = len(s)
    for l in range(1,int(len(s)/2)+1):
        encoded = ''
        idx = 0
        matched = s[:l]
        count = 0
        while idx < len(s):
            if matched == s[idx:idx+l]:
                count += 1
            else:
                if count > 1:
                    encoded += str(count) + matched
                else:
                    encoded += matched
                count = 1
                matched = s[idx:idx+l]
            idx += l
        if count > 1:
            encoded += str(count) + matched
        else:
            encoded += matched
        answer = min(answer, len(encoded))
    return answer