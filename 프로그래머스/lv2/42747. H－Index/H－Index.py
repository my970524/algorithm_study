def solution(citations):
    citations.sort(reverse=True)
    print(citations)

    for c in range(citations[0], 0, -1):
        over_citations = len(list(filter(lambda x: x >= c, citations)))
        less_citations = len(list(filter(lambda x: x <= c, citations)))
        if over_citations >= c and less_citations <= c:
            return c
    return 0
