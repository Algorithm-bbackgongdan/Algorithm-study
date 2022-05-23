def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    ls = sorted([list(map(int, e.split(","))) for e in s], key=lambda x : len(x))
    answer.append(ls[0][0])
    prev_set = set(ls[0])
    for elem in ls[1:]:
        curr_set = set(elem)
        answer.append(list(curr_set - prev_set)[0])
        prev_set = curr_set
    return answer