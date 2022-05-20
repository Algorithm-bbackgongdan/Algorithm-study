def solution(s):
    input_list = s[2:-2].split('},{')
    answer = []
    input_list.sort(key=lambda x : len(x))
    
    for element in input_list:
        level = element.split(',')
        for temp in level:
            if int(temp) not in answer:
                answer.append(int(temp))
                break
    
    return answer