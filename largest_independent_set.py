import random
import time

def find_largest_independent_set(matrix):
    
    n = len(matrix)
    
    #create adjacency list from given matrix
    edges = {}
    for i in range(0,n):
        conn_node = []
        for j in range(0,n):
            if matrix[i][j] != 0:
                conn_node.append(j+1)
            edges[i+1] = conn_node

    independent_sets = []
    for val in edges:
        ind_set = find_independent_set(val,edges)
        if ind_set not in independent_sets:
            independent_sets.append(ind_set)
    
    max = 2
    length = len(independent_sets)
    for i in range(0,length):
        max_val = len(independent_sets[i])
        if max_val > max:
            max = max_val
    
    for i in range(0,length):
        if len(independent_sets[i]) == max:
            print independent_sets[i]

def find_independent_set(val,edges):
    #variable for total number of vertices
    nodes = range(1,len(edges)+1)
    
    for node in edges[val]:
        if node in nodes:
            nodes.remove(node)

    for value in nodes:
        if value != val:
            for node in edges[value]:
                if node in nodes:
                    nodes.remove(node)    

    return nodes

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

    #Find if the graph contains circle

    start_time = time.time()

    matrix = generate_random_graph(200)
    find_largest_independent_set(matrix)

    print("Time to compute the largest independent set is", (time.time() - start_time))
        

if __name__ == "__main__":
    main()