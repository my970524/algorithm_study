from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    n = len(priorities)
    docs = deque([chr(i) for i in range(97, 97+n)])
    my_doc = docs[location]
    answer = 0

    while my_doc in docs:
        priority = priorities.popleft()
        doc = docs.popleft()
        if any(priority < p for p in priorities):
            priorities.append(priority)
            docs.append(doc)
        else:
            answer += 1
    return answer