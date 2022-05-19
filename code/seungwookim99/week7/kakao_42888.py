def solution(record):
    answer = []
    nickname = {}
    for r in record:
        data = r.split(" ")
        if data[0] == "Leave":
            continue
        nickname[data[1]] = data[2]
    
    for r in record:
        data = r.split(" ")
        if data[0] == "Leave":
            msg = f"{nickname[data[1]]}님이 나갔습니다."
        elif data[0] == "Enter":
            msg = f"{nickname[data[1]]}님이 들어왔습니다."
        else:
            continue
        answer.append(msg)
    return answer