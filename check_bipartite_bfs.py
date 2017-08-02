def find_bipartite(matrix):
    
    n = len(matrix)
    #create adjacency list from given matrix
    edges = {}
    for i in range(0,n):
        conn_node = []
        for j in range(0,n):
            if matrix[i][j] != 0:
                conn_node.append(j+1)
            edges[i+1] = conn_node

    bipartite_dict = bfs(edges)

    #Check if it is bipartite
    for node in edges:
        for edge in edges[node]:
            if bipartite_dict[edge] == bipartite_dict[node]:
                return False
    return True

def bfs(edges):
    #variables
    node_list = [1]
    visited_nodes = []
    bool_dict = {1:True}

    #Iterate in breadth first manner and create a bool_dict
    while node_list:
        temp_list = []
        for node in node_list:
            visited_nodes.append(node)
            for adj_node in edges[node]:
                if adj_node not in visited_nodes:
                    temp_list.append(adj_node)
                    bool_dict[adj_node] = not bool_dict[node]
        node_list = temp_list

    return bool_dict

def main():

    #Testcase 1
    #matrix = [[0,5,4,0,0,0,0],[5,0,0,0,0,0,0],[4,0,0,0,0,9,7],[0,0,0,0,0,0,1],
    #          [0,0,0,0,0,0,3],[0,0,9,0,0,0,0],[0,0,7,1,3,0,0]]
    
    #Testcase 2
    #matrix = [[0,21,0,0,0,0,0,0,29,0],[21,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,24,0],
    #          [0,0,0,0,16,0,0,0,0,10],[0,0,0,16,0,0,24,0,7,0],[0,0,0,0,0,0,5,0,23,8],
    #          [0,0,0,0,24,5,0,13,0,0],[0,0,0,0,0,0,13,0,13,0],[29,0,24,0,7,23,0,13,0,0],
    #          [0,0,0,10,0,8,0,0,0,0]]
    
    #Testcase 3
    matrix = [[0,0,0,16,12,20,18,10,0,0,18,0,0,0,28],[0,0,0,17,24,14,0,0,0,23,10,6,0,26,20],
              [0,0,0,0,19,0,0,0,0,0,0,0,26,14,0],[16,17,0,0,0,15,0,23,0,0,0,0,0,24,28],
              [12,24,19,0,0,0,0,0,0,0,21,0,9,29,0],[20,14,0,15,0,0,0,9,6,0,26,0,0,20,0],
              [18,0,0,0,0,0,0,0,0,0,13,15,0,0,5],[10,0,0,23,0,9,0,0,8,14,17,0,12,0,0],
              [0,0,0,0,0,6,0,8,0,0,0,29,22,0,28],[0,23,0,0,0,0,0,14,0,0,20,0,18,0,25],
              [18,10,0,0,21,26,13,17,0,20,0,0,11,22,16],[0,6,0,0,0,0,15,0,29,0,0,0,0,14,24],
              [0,0,26,0,9,0,0,12,22,18,11,0,0,0,22],[0,26,14,24,29,20,0,0,0,0,22,14,0,0,0],
              [28,20,0,28,0,0,5,0,28,25,16,24,22,0,0]]

    #Find if the graph is bipartite
    if find_bipartite(matrix):
        print "Yes, the graph is bipartite"
    else:
        print "No, the graph is not bipartite"

if __name__ == "__main__":
    main()