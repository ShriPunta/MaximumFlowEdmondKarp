"""
used as a library to compute longest path
"""
"""
The parameters used throughout the code are:
    G : It is the networkX graph object
    v : It is the node of the graph to start DFS
    path : path of the graph
    seen : set of seen nodes

This function is used to calculate the DFS path from the vertex v
"""
seen=set()
def DFS(G,v,path=None):
    #if seen is None: seen = set()
    if path is None: path = [v]
    seen.add(v)
    #print(seen)
    #path_list is to maintain the traversed path
    path_list = []
    for t in G[v]:
        if t not in seen:
            t_path = path + [t]
            path_list.append(tuple(t_path))
            path_list.extend(DFS(G, t, t_path))
    return path_list

#This function is used as driver to calculate the longest path using the DFS
def run_the_algo(capMat):
    # Run DFS, compute all paths in the graph
    all_paths = [p for ps in [DFS(capMat, n) for n in set(capMat)] for p in ps]
    # choose the path with max length
    max_len = max(len(p) for p in all_paths)
    # store the path with maximum length
    max_paths = [p for p in all_paths if len(p) == max_len]

    # Output
    print("Longest Paths:")
    for p in max_paths:
        print(" -> ", p)

    print("Longest Path Length:")
    print(max_len)

    return (all_paths, max_len, max_paths)