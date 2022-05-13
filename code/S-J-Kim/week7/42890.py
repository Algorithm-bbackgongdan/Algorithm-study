from itertools import combinations


def solution(relation):
    iterlist = [i for i in range(len(relation[0]))]

    cardinality = len(relation)
    candkey = set()

    for i in range(1, len(relation[0]) + 1):
        for com in combinations(iterlist, i):
            keys = []

            for tp in relation:
                key = [tp[attr] for attr in com]

                if key in keys:
                    break
                else:
                    keys.append(key)

            if len(keys) == cardinality:
                for key in candkey:
                    if set(key).issubset(com):
                        break

                else:
                    candkey.add(com)

    return len(candkey)


solution(
    [
        ["100", "ryan", "music", "2"],
        ["200", "apeach", "math", "2"],
        ["300", "tube", "computer", "3"],
        ["400", "con", "computer", "4"],
        ["500", "muzi", "music", "3"],
        ["600", "apeach", "music", "2"],
    ]
)
