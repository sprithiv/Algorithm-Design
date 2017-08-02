import random
import time

def find_largest_complete_subgraph(matrix):
    
    n = len(matrix)
    
    #create adjacency list from given matrix
    edges = {}
    for i in range(0,n):
        conn_node = []
        for j in range(0,n):
            if matrix[i][j] != 0:
                conn_node.append(j+1)
            edges[i+1] = conn_node

    complete_subgraph = []
    for val in edges:
        comp_graph = find_complete_subgraph(val,edges)
        comp_graph.sort()
        if comp_graph not in complete_subgraph:
            complete_subgraph.append(comp_graph)
    
    max = 2
    length = len(complete_subgraph)
    for i in range(0,length):
        max_val = len(complete_subgraph[i])
        if max_val > max:
            max = max_val
    
    for i in range(0,length):
        if len(complete_subgraph[i]) == max:
            print complete_subgraph[i]
            return
    
def find_complete_subgraph(val,edges):
    subgraph = [val]
    subgraph.extend(edges[val])

    for value in subgraph:
        for sub_value in subgraph:
            if sub_value not in edges[value]:
                if value != sub_value:
                    subgraph.remove(sub_value)

    return subgraph

def generate_random_graph(n):
    a = []
    for i in range(0,n):
        a.append([])
        for j in range(0,n):
            a[i].append(0)
    for i in range(0,n):
        for j in range(0,i):
                a[i][j] = a[j][i] = random.randint(0,1)
    return a

def main():

    #Testcase 1
    #matrix = [[0,1,0,1,1,0,0],[1,0,1,1,0,1,0],[0,1,0,1,1,1,1],
    #          [1,1,1,0,1,1,0],[1,0,1,1,0,1,0],[0,1,1,1,1,0,0],
    #          [0,0,1,0,0,0,0]]

    #Testcase 2
    #matrix = [[0,0,1,0,0,1,0,1,1,0,0],[0,0,1,1,1,0,0,1,1,0,1],[1,1,0,1,1,0,1,0,1,0,1],
    #          [0,1,1,0,1,0,1,1,1,0,0],[0,1,1,1,0,1,1,0,1,1,0],[1,0,0,0,1,0,1,1,1,1,1],
    #          [0,0,1,1,1,1,0,1,1,0,0],[1,1,0,1,0,1,1,0,1,0,1],[1,1,1,1,1,1,1,1,0,0,1],
    #          [0,0,0,0,1,1,0,0,0,0,1],[0,1,1,0,0,1,0,1,1,1,0]]

    start_time = time.time()

    matrix = generate_random_graph(2000)
    find_largest_complete_subgraph(matrix)

    print("Time to compute the largest clique set is", (time.time() - start_time))

if __name__ == "__main__":
    main()