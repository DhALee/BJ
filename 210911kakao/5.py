def dfs(info, graph, start_node):
    visit = []
    stack = []
    one_return = True

    stack.append(start_node)
    sheep = 0
    wolf = 0
    while stack:
        node = stack.pop()
        if info[node]:
            wolf += 1
        else:
            sheep += 1
        print(node, sheep, wolf)
        if node not in visit and sheep > wolf:
            visit.append(node)                
            stack.extend(reversed(graph[node]))

        if sheep == wolf and one_return:
            visit.append(node)
            for _ in range(sheep):
                wolf -= 1
            stack.insert(0, visit.pop())
            one_return = False
            
        # if len(info) - 1 == node:
        #     while info[visit.pop()] == 1:
        #         wolf -= 1

        if info[node] == 1 and graph[node] == [] and one_return is False:
            visit.pop()
            wolf -= 1


    return sheep

def solution(info, edges):
    answer = 0
    graph = [[] for _ in range(len(info))]
    for start, end in edges:
        graph[start].append(end)
    
    answer = dfs(info, graph, 0)
    print(answer)
    return answer


# solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])
solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]])