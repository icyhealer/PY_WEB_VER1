seoul = ["Jane", "Kim"]

def solution (aList):
    count = 0
    answer = ""
    for aPerson in seoul:
        if aPerson == "Kim":
            answer = "김서방은 "+str(count)+"에 있다."
            count += 1

    return answer

print(solution(seoul))