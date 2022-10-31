import copy

def dfs(graph, start, visited):
    count = 0
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)
            count += 1
    return visited


def solution(n , wires):
    answer = n - 2

    for i in range(len(wires)):
        new_wires = copy.deepcopy(wires)
        new_wires.pop(i)
        # dfs를 위한 그래프와 visited 리스트 만들기
        graph = [[] for i in range(n+1)]
        visited = [False] * (n+1)

        for wire in new_wires:
            graph[wire[0]].append(wire[1])
            graph[wire[1]].append(wire[0])
    
        for i, g in enumerate(graph):
            if g:
                start = i
                break
        count = dfs(graph, start, visited).count(True)
        diff = abs(count - (n - count))

        answer = min(answer, diff)

    return answer