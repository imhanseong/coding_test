def solution(intStrs, k, s, l):
    answer = []
    for x in intStrs :
        if k < int(x[s:s+l]) :
            answer.append(int(x[s:s+l]))
    return answer