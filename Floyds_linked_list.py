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
def shortestpath(distance,sequence,start_node,end_node):

    short_path_list = LinkedList()
    start_time = time.time()
    n = len(distance)
    for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                short_path_list.add(distance[i][j])

    iteration = 0
    k = 0
    
    while iteration < n:
        for i in range(0,n):
            for j in range(0,n):
                if i != j and i !=iteration and j != iteration:
                    value = i * n + j
                    initial_value = short_path_list.get_val(value)
                    comp_val = short_path_list.get_val(i * n + iteration) + short_path_list.get_val(iteration * n + j)
                    short_path_list.set_val(i * n +j , min(short_path_list.get_val(i * n + j),comp_val))
                    if initial_value != short_path_list.get_val(i * n + j):
                        sequence[i][j] = iteration+1
                    
        iteration += 1

    shortest_path = short_path_list.get_val((start_node-1 )* n + (end_node-1))
    print "The shortest path from node", start_node , "to", end_node , "is", shortest_path

    flag = 0
    if start_node < end_node:
        start_node,end_node = end_node,start_node
        flag = 1

    shortest_path = [start_node]
    val = sequence[start_node-1][end_node-1]
    if val != end_node:
        mid_node = val
        while shortest_path[-1] != end_node:
            shortest_path.append(mid_node)
            mid_node = sequence[mid_node-1][end_node-1]
    else:
        shortest_path.append(end_node)

    if flag == 1:
        shortest_path.reverse()

    print "The path is" + " " + ' -> '.join(map(str,shortest_path))
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

#Function to generate the sequential matrix
def generate_sequential_matrix(n):
    b = []
    for i in range(0,n):
        b.append([])
        for j in range(0,n):
            if i == j:
                b[i].append("")
            else:
                b[i].append(j+1)
    return b

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
    #distance = [["",11,14,99,8,99,29,28,99,99,14,99],[11,"",12,99,6,99,99,99,99,99,99,99],
    #           [14,12,"",18,13,13,99,99,25,99,99,16],[99,99,18,"",99,99,27,17,9,25,99,99],
    #            [8,6,13,99,"",99,99,99,99,99,99,22],[99,99,13,99,99,"",99,15,5,99,99,99],
    #            [29,99,99,27,99,99,"",99,99,99,99,99],[28,99,99,17,99,15,99,"",5,9,99,99],
    #            [99,99,25,9,99,5,99,5,"",99,25,99],[99,99,99,25,99,99,99,9,99,"",99,99],
    #            [14,99,99,99,99,99,99,99,25,99,"",99],[99,99,16,99,22,99,99,99,99,99,99,""]]

    sequence = generate_sequential_matrix(n)

    start_node = int(raw_input("Please enter the start node: "))
    end_node = int(raw_input("Please enter the end node: "))

    shortestpath(distance,sequence,start_node,end_node)

if __name__ == "__main__":
    main()
