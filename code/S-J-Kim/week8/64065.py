def solution(s):
    answer = []
    tmpset = set()

    s = "(" + s[2:-2] + ")"

    setarr = s.replace("},{", ")(").replace(",", "/").replace(")(", "),(").split(",")

    for (i, el) in enumerate(setarr):
        setarr[i] = set(el[1:-1].split("/"))

    setarr.sort(key=lambda x: len(x))

    for el in setarr:
        diff = el.difference(tmpset)
        answer.append(int(*diff))
        tmpset.add(*diff)

    return answer


solution(r"{{2},{2,1},{2,1,3},{2,1,3,4}}")

# 집합을 원소의 길이 오름차순으로 정렬
# 제일 작은 크기의 원소부터 set에 넣으면서 다음 길이로 넘어간다
# 차집합을 끝에 더한다
