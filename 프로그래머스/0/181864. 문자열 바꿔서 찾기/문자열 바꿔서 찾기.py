def solution(my, pat):
    answer = 0
    my = list(my)
    for a in range(len(my)):
        if my[a] == "A":
            my[a] = "B"
        else:
            my[a] = "A"
    if pat in "".join(my):
        answer = 1
    return answer
