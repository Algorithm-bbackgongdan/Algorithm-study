from collections import defaultdict


def solution(record):
    answer = []
    nickmap = defaultdict(str)
    enter = []

    message = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}

    for rec in record:
        rec = rec.split()
        action = rec[0]
        uid = rec[1]

        if action == "Enter" or action == "Leave":
            enter.append(f"{action} {uid}")

        if action == "Enter" or action == "Change":
            nickmap[uid] = rec[2]

    for command in enter:
        action, uid = command.split()

        answer.append(f"{nickmap[uid]}{message[action]}")

    return answer


solution(
    [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan",
    ]
)


# uid: 닉네임 관계의 딕셔너리 선언
# enter, leave: uid 관계의 리스트 선언
# 이후 순차 출력
