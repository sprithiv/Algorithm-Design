def find_cyclic(matrix):
    
    n = len(matrix)
    
    #create adjacency list from given matrix
    edges = {}
    for i in range(0,n):
        conn_node = []
        for j in range(0,n):
            if matrix[i][j] != 0:
                conn_node.append(j+1)
            edges[i+1] = conn_node

    #Variables for calling depth first search function
    initial_node = 1
    visited_nodes = []
    depth_level = 0
    parent = 1
    #Calling the depth first serach function
    if dfs(initial_node , edges, visited_nodes, depth_level, parent):
        return True
    return False

def dfs(node, edges, visited_nodes, depth_level, parent):
    #variable for tracking the visited nodes
    visited_nodes.append(node)
    #Depth first search algorithm to find if the graph is cyclic
    for adj_node in edges[node]:
        if adj_node in visited_nodes and depth_level > 1 and adj_node != parent:
            return True
        elif adj_node not in visited_nodes:
            depth_level += 1
            #Recursive call
            if dfs(adj_node, edges, visited_nodes, depth_level, node):
                return True

    return False

def main():

    #Testcase 1
    #matrix = [[0,12,14,0,0,0,0,20],[12,0,10,6,28,0,0,0],[14,10,0,0,0,11,0,0],
    #          [0,6,0,0,0,0,19,0],[0,28,0,0,0,0,0,0],[0,0,11,0,0,0,0,0],
    #          [0,0,0,19,0,0,0,24],[20,0,0,0,0,0,24,0]]

    #Testcase 2
    #matrix = [[0,5,6,0,0,0],[5,0,0,7,8,9],[6,0,0,0,0,0],[0,7,0,0,0,0],
    #          [0,8,0,0,0,0],[0,9,0,0,0,0]]

    #Testcase 3
    matrix = [[0,0,24,0,0,0,0,0,5,0,17,0,24,0,0],[0,0,0,0,20,24,10,5,17,0,15,0,0,0,0],
              [24,0,0,0,0,0,0,0,28,0,0,14,10,0,0],[0,0,0,0,26,0,26,0,0,22,0,0,0,6,22],
              [0,20,0,26,0,0,0,0,26,0,0,17,0,0,11],[0,24,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,10,0,26,0,0,0,0,7,0,0,7,0,0,0],[0,5,0,0,0,0,0,0,0,18,20,16,0,0,0],
              [5,17,28,0,26,0,7,0,0,0,24,7,0,0,0],[0,0,0,22,0,0,0,18,0,0,0,0,0,19,0],
              [17,15,0,0,0,0,0,20,24,0,0,0,0,0,19],[0,0,14,0,17,0,7,16,7,0,0,0,0,0,0],
              [24,0,10,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,6,0,0,0,0,0,19,0,0,0,0,27],
              [0,0,0,22,11,0,0,0,0,0,19,0,0,27,0]]

    #Find if the graph contains circle
    if find_cyclic(matrix):
        print "Yes, the graph contains circle"
    else:
        print "No, the graph doesn't contain circle"

if __name__ == "__main__":
    main()