def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return n * c_lib

    # construct adjacency list
    neighbor = {}
    for c in cities:
        neighbor[c[0]-1] = neighbor.get(c[0]-1, []) + [c[1]-1]
        neighbor[c[1]-1] = neighbor.get(c[1]-1, []) + [c[0]-1]
    
    visited = [False] * n
    nodes_in_cluster = {}
    num_cluster = 0
    def dfs(node, cluster):
        if visited[node] == False:
            nodes_in_cluster[cluster] = nodes_in_cluster.get(cluster, 0) + 1
            visited[node] = True
            my_neighbor = neighbor.get(node, [])
            if len(my_neighbor) != 0: #isloated node
                for city_id in my_neighbor:
                    if visited[city_id] == False:
                        dfs(city_id, cluster)
  
    for i in range(n):
        if visited[i] == False:
            num_cluster += 1
            dfs(i, i)

    # count total roads need to build and total cost
    roads = sum(x-1 for x in nodes_in_cluster.values())
    total = c_road * roads + c_lib * num_cluster
    return total
