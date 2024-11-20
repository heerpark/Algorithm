def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    head = 0
    tail = len(people) - 1
    while (head < tail):
        if people[head] + people[tail] > limit:
            head += 1
            answer += 1
        else:
            head += 1
            tail -= 1
            answer += 1
    if head == tail:
        answer += 1
    return answer