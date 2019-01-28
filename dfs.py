def dfsrecursive(adj_list,tgt):
    visited = []
    for i in adj_list:
        visited.append(i)
    for i in range(len(visited)):
	    if(visited[i] != -1):
                dfshelper(visited[i],visited,adj_list,tgt)

def dfshelper(node,visited,adj_list,tgt):
    visited[visited.index(node)] = -1
    print(node)
    print(visited)
    for i in adj_list:
        if(i in visited):
            dfshelper(i,visited,adj_list,tgt)

if __name__ == "__main__":
    adj_list = {
        1:[4,5],
        2:[5,1],
        5:[4,1,3],
        3:[2,4],
        4:[2,1]
    }
    print(len(adj_list))
    dfsrecursive(adj_list,3)
