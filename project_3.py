#Group 3
#Project 3
#March 26, 2023


def prims(edges):

    #starts by initializing a set called visited to
    #keep track of the visited nodes. It then chooses a starting node
    #from the first node in the graph and adds it to the visited set. An
    #empty list called mst is also initialized
    #to keep track of the edges in the minimum spanning tree.
    
    visited = set()  # set to keep track of visited nodes
    start = edges[0][0]  # starting node
    visited.add(start)
    
    tree = []  #place to hold minimum spanning tree
    total_cost = 0


    #while loop runs until all nodes in the graph have
    #been visited. In each iteration of the loop, the algorithm checks
    #all edges that connect visited and unvisited nodes. It chooses the
    #edge with the smallest weight and adds its two endpoints
    #to the visited set. The chosen edge is then added to the tree list.
    
    while len(visited) < len(edges):
        min_edge = None
        for node in visited:
            for edge in edges:
                if node == edge[0] and edge[1] not in visited:
                    if min_edge is None or edge[2] < min_edge[2]:
                        min_edge = edge
                elif node == edge[1] and edge[0] not in visited:
                    if min_edge is None or edge[2] < min_edge[2]:
                        min_edge = edge
        if min_edge is not None:
            visited.add(min_edge[0])
            visited.add(min_edge[1])
            tree.append(min_edge)
            print(min_edge)#prints out the path of minimum spanning tree
            total_cost += min_edge[2]
            print("total cost:" + str(total_cost))#prints out the cost of path
            

    return tree #debug issue: not returning the tree in single array??
    return total_cost #debug issue: not returning the tree in single array??

    ##Tasks to do:
    #print out path: Done 
    #print out total cost: Not done



# Open the file and read the contents
with open('edgeList.txt', 'r') as file:
    contents = file.read()

# Split the contents into a list of strings
string_list = contents.split('\n')

# Remove any empty strings
string_list = [string for string in string_list if string]

# Split each string into a tuple of integers
edges = [tuple(map(int, string.split(','))) for string in string_list]

#runs program 
tree = prims(edges)
print(total_cost)

