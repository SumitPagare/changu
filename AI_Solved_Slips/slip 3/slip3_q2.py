graph = {
  '1' : ['2','3'],
  '2' : ['4'],
  '3' : ['2'],
  '4' : ['5', '6'],
  '5' : ['3', '7'],
  '6' : [],
  '7' : ['6']
}

def dfs_path(graph, start, goal, path=[]):
    path = path + [start]
    if start == goal:
        return path
    if start not in graph:
        return None
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs_path(graph, neighbor, goal, path)
            if new_path:
                return new_path
    return None

# Driver Code
start_node = '1'
goal_node = '7'
result_path = dfs_path(graph, start_node, goal_node)

if result_path:
    print(f"Path from {start_node} to {goal_node}: {result_path}")
else:
    print(f"No path found from {start_node} to {goal_node}")
