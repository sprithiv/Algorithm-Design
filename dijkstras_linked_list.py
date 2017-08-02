import random
import time

class Node :
	def __init__( self, data) :
		self.data = data
		self.next = None
		self.prev = None

class LinkedList :
	def __init__( self ) :
		self.head = None

	def add( self, data ) :
		node = Node( data )
		if self.head == None :	
			self.head = node
		else :
			node.next = self.head					
			self.head = node	

	def get_val(self, position) :
		p = self.head
		count = 0
		if position == 0 and p != None:
			return p.data
		else:				
			while (p):
				if (count == position):
					return p.data
				count += 1
				p = p.next

	def set_val(self, position, data) :
		p = self.head
		count = 0
		if position == 0 and p != None:
			p.data = data
		else:				
			while (p):
				if (count == position):
					p.data = data
				count += 1
				p = p.next

	def get_list( self ) :
		s = []
		p = self.head
		if p != None :		
			while p.next != None :
				s.append(p.data)
				p = p.next
			s.append(p.data)
		return s

#Function to find the shortest path of the given graph
def shortestpath(distance,start_node,end_node):
    
	start_time = time.time()
	
    adjacency_list = LinkedList()

    n = len(distance)
    unvisited_nodes = []
    for i in range(1,n+1):
        unvisited_nodes.append(i)

    for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                adjacency_list.add(distance[i][j])

    edges = {}
    distances = {}
    for i in range(0,n):
        conn_node = []
        for j in range(0,n):
            if adjacency_list.get_val(i*n+j) != 0 and adjacency_list.get_val(i*n+j) < 99:
                conn_node.append(j+1)
        edges[i+1] = conn_node

    visited_nodes = {}
    visited_nodes[start_node] = 0
    path = {}

    while unvisited_nodes:
        min_node = None
        for node in unvisited_nodes:
            if node in visited_nodes:
                if min_node is None:
                    min_node = node
                elif visited_nodes[node] < visited_nodes[min_node]:
                    min_node = node
        if min_node is None:
            break

        unvisited_nodes.remove(min_node)
        current_dist = visited_nodes[min_node]

        for edge in edges[min_node]:
            dist = current_dist + adjacency_list.get_val((min_node-1)*n+(edge-1))
            if edge not in visited_nodes or dist < visited_nodes[edge]:
                visited_nodes[edge] = dist
                path[edge] = min_node

    #full_path = []
    full_path = LinkedList()
    destination = path[end_node]

    full_path.add(end_node)
    
    while destination != start_node:
        full_path.add(destination)
        destination = path[destination]
    
    full_path.add(start_node)
    shortest_path = visited_nodes[end_node]

    print "The shortest path from node", start_node , "to", end_node , "is", shortest_path
    print "The path is" + " " + ' -> '.join(map(str,full_path.get_list()))
	print("Time to compute the shortest path matrix", (time.time() - start_time))

#Function to generate a complete graph
def generate_complete_graph(n):
    a = []
    for i in range(0,n):
        a.append([])
        for j in range(0,n):
            a[i].append("")
    for i in range(0,n):
        for j in range(0,i):
                a[i][j] = a[j][i] = random.randint(1,30)
    return a

#Function to generate the sparse graph
def generate_sparse_graph(n):
    a = []
    for i in range(0,n):
        a.append([])
        for j in range(0,n):
            a[i].append("")
    for i in range(0,n):
        for j in range(0,i):
                a[i][j] = a[j][i] = random.randint(1,40)

    for i in range(0,n):
        for j in range(0,n):
            if i != j:
                if a[i][j] > 30:
                    a[i][j] = 99
    return a


def main():

    #Modify the number of nodes in the graph
    n = 10
    #Generates a complete graph with random numbers for the given number of nodes
    distance = generate_complete_graph(n)

    #Generates a sparse graph with random numbers between 1 to 30, with given number of nodes
    #distance = generate_sparse_graph(n)

    # Test case 1(Nodes which are not connected directly are considered as infinity and value 99 is used)
    #distance = [[0,99,99,29,99,99,99,99],[99,0,99,99,99,11,11,99],
    #            [99,99,0,12,99,5,5,99],[29,99,12,0,5,99,13,99],
    #           [99,99,99,5,0,99,7,11],[99,11,5,99,99,0,99,17],
    #            [99,11,5,13,7,99,0,99],[99,99,99,99,11,17,99,0]]
    
    #Test case 2(Nodes which are not connected directly are considered as infinity and value 99 is used)
    #distance = [[0,11,14,99,8,99,29,28,99,99,14,99],[11,0,12,99,6,99,99,99,99,99,99,99],
    #           [14,12,0,18,13,13,99,99,25,99,99,16],[99,99,18,0,99,99,27,17,9,25,99,99],
    #            [8,6,13,99,0,99,99,99,99,99,99,22],[99,99,13,99,99,0,99,15,5,99,99,99],
    #            [29,99,99,27,99,99,0,99,99,99,99,99],[28,99,99,17,99,15,99,0,5,9,99,99],
    #            [99,99,25,9,99,5,99,5,0,99,25,99],[99,99,99,25,99,99,99,9,99,0,99,99],
    #            [14,99,99,99,99,99,99,99,25,99,0,99],[99,99,16,99,22,99,99,99,99,99,99,0]]

    start_node = int(raw_input("Please enter the start node: "))
    end_node = int(raw_input("Please enter the end node: "))

    shortestpath(distance,start_node,end_node)

if __name__ == "__main__":
    main()
