def solution(s):
    answer = len(s)

    for i in range(1, len(s)):
        tmpstr = s[:]
        tmpans = 0

        prestr = tmpstr[:i]
        ziplen = 1

        while len(tmpstr) >= i:
            tmpstr = tmpstr[i:]

            if tmpstr[:i] == prestr:
                ziplen += 1

            else:
                if ziplen > 1:
                    tmpans += len(str(ziplen)) + len(prestr)

                else:
                    tmpans += len(prestr)

                ziplen = 1
                prestr = tmpstr[:i]

        tmpans += len(tmpstr)

        answer = min(answer, tmpans)

    return answer


solution("aabbaccc")

# i에 대해서 문자열 i까지 보고 현재 문자열로 설정
# 그 길이만큼 잘라버린 다음에 처음 문자열이 현재 설정 문자열과 같으면 압축 길이 증가
# 달라지면 처음 문자열 길이 * 압축크기 더한다음 처음 문자열 교체
# 남은 문자열이 i보다 작아지면 그냥 길이 더함
