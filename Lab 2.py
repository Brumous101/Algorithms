# Kyle Johnson
# ETEC3401 9:00 AM
# Prof. Skaggs
# 12-6-20
# Lab 2 - Graph Traversal and Path Search

import string

#class GRAPH(object):
#    def __init__(self, cities, distances, roads, start_city, final_city):
#        self.distances = distances
#        self.cities = cities
#        self.roads = roads
#        self.start_city = start_city
#        self.final_city = final_city
#        self.city= self.start_city
#    def run_algorithm(self):
#        totalDistance = 0
#        i=0
#        templist = list()
#        visitedlist = list()
#        for a in self.cities:
#            a[2] = float('inf')
#            if a[0] == self.start_city:
#                a[2] = 0
#                a[1] = 'current'
#
#        while(i <4):
#            i = i + 1
#            shortestDistance = 0
#            templist.append([])
#            templist.append([]) 
#            for b in self.roads:
#                if len(visitedlist) > 0:
#                    for c in range(len(visitedlist)):
#
#                        #It is still adding them because the [c] index is bad for the if check
#
#                        if b[0]== self.city and b[0] != visitedlist[c] and b[2] != visitedlist[c]:
#                            templist[0].append(b[2])
#                            templist[1].append(b[1])
#                            #print(visitedlist[c])
#                            
#                        if b[2]== self.city and b[2] != visitedlist[c] and b[0] != visitedlist[c]:
#                            templist[0].append(b[0])
#                            templist[1].append(b[1])
#                            #print(visitedlist[c])
#                else:
#                    if b[0]== self.city:
#                        templist[0].append(b[2])
#                        templist[1].append(b[1])
#                        
#                    if b[2]== self.city:
#                        templist[0].append(b[0])
#                        templist[1].append(b[1])
#            #print("something")
#            #print(self.city)
#            #print("visited")
#            #print(visitedlist)
#            #print("temp")
#            #print(templist)
#            #print(templist)
#            shortestDistance = templist[1][0]
#            for d in range(len(templist[1])):
#                if int(shortestDistance) > int(templist[1][d]):
#                    shortestDistance = templist[1][d]
#            print(shortestDistance)
#            for c in range(len(self.cities)):
#                for d in range(len(templist[0])):
#                    if self.cities[c][0] == templist[0][d] and self.cities[c][1] != "visited": # names match
#                        self.cities[c][2] = templist[1][d] # append distance from start
#                        self.cities[c][1] = "considering" # append distance from start
#            for c in range(len(self.cities)):
#                for d in range(len(templist[0])):
#                    if self.cities[c][0] == templist[0][d] and self.cities[c][1] != "visited": # names match
#                        if self.cities[c][1] == "considering": # possibly it match
#                            if self.cities[c][2] == shortestDistance: # road match!
#                                for a in self.cities:
#                                    if a[0] == self.city:
#                                        visitedlist.append(self.city)
#                                        a[1] = 'visited'
#                                totalDistance += int(shortestDistance)
#                                self.cities[c][1] = "current"
#                                self.city = self.cities[c][0]
#                            else:
#                                if self.cities[c][1] == "considering":
#                                    self.cities[c][1] = "unvisited"
#            templist.clear()
#            if self.final_city == self.city:
#                return True
#
#        
#    def reset(self):
#        self.city=self.start_city
#    def state_accepting(self):
#        return False 
#
#dijkstras_algorithm = GRAPH(
#        cities=[['Oradea','unvisited','distance'],['Zerind','unvisited','distance'],['Arad','unvisited','distance'],['Timisoara','unvisited','distance'],['Lugoj','unvisited','distance'],['Mehadia','unvisited','distance'],['Drobeta','unvisited','distance'],['Craiova','unvisited','distance'],['Riminicu Vilcea','unvisited','distance'],['Sibiu','unvisited','distance'],['Fagaras','unvisited','distance'],['Pitesti','unvisited','distance'],['Bucharest','unvisited','distance'],['Giurgiu','unvisited','distance'],['Urzieeni','unvisited','distance'],['Hirsova','unvisited','distance'],['Eforie','unvisited','distance'],['Vaslui','unvisited','distance'],['Iasi','unvisited','distance'],['Neamt','unvisited','distance']],
#        distances=['71','75','118','111','70','140','151','120','80','99','97','146','138','101','211','90','85','87','92','142','98','86'],
#        roads=[
#        ['Oradea','151','Sibiu'],
#        ['Oradea','71','Zerind'],
#        ['Zerind','75','Arad'],
#        ['Arad','118','Timisoara'],
#        ['Timisoara','111','Lugoj'],
#        ['Lugoj','70','Mehadia'],
#        ['Mehadia','75','Drobeta'],
#        ['Drobeta','120','Craiova'],
#        ['Craiova','146','Riminicu Vilcea'],
#        ['Craiova','138','Pitesti'],
#        ['Pitesti','97','Riminicu Vilcea'],
#        ['Riminicu Vilcea','80','Sibiu'],
#        ['Sibiu','140','Arad'],
#        ['Sibiu','99','Fagaras'],
#        ['Fagaras','211','Bucharest'],
#        ['Bucharest','90','Giurgiu'],
#        ['Bucharest','101','Pitesti'],
#        ['Bucharest','85','Urzieeni'],
#        ['Urzieeni','98','Hirsova'],
#        ['Hirsova','86','Eforie'],
#        ['Urzieeni','142','Vaslui'],
#        ['Vaslui','92','Iasi'],
#        ['Iasi','87','Neamt']],
#        start_city='Arad', # Maybe could make user input
#        final_city='Bucharest' # Maybe user input
#    )

#string = input("Enter a start city: ")
#string = input("Enter a final city: ")

#dijkstras_algorithm.reset()
#print("Test: ->",dijkstras_algorithm.run_algorithm())



graph={'Oradea':{'Sibiu':151,'Zerind':71},
        'Zerind':{'Arad':75,'Oradea':71},
        'Arad':{'Timisoara':118,'Sibiu':140,'Zerind':75},
        'Timisoara':{'Lugoj':111,'Arad':118},
        'Lugoj':{'Timisoara':111,'Mehadia':70},
        'Mehadia':{'Lugoj':70,'Drobeta':75},
        'Drobeta':{'Mehadia':75,'Craiova':120},
        'Craiova':{'Drobeta':120,'Pitesti':138,'Riminicu Vilcea':146},
        'Pitesti':{'Craiova':138,'Bucharest':101,'Riminicu Vilcea':97},
        'Riminicu Vilcea':{'Pitesti':97,'Craiova':146,'Sibiu':80},
        'Sibiu':{'Riminicu Vilcea':80,'Arad':140,'Fagaras':99,'Oradea':151},
        'Fagaras':{'Sibiu':99,'Bucharest':211},
        'Bucharest':{'Fagaras':211,'Giurgiu':90,'Pitesti':101,'Urzieeni':85},
        'Hirsova':{'Urzieeni':98,'Eforie':86},
        'Urzieeni':{'Bucharest':85,'Hirsova':98,'Vaslui':142},
        'Vaslui':{'Urzieeni':142,'Iasi':92},
        'Iasi':{'Vaslui':92,'Neamt':87},
        'Neamt':{'Iasi':87},
        'Eforie':{'Hirsova':86},
        'Giurgiu':{'Bucharest':90}}
graph2={'Oradea':{'Sibiu':151,'Zerind':71},
        'Zerind':{'Arad':75,'Oradea':71},
        'Arad':{'Timisoara':118,'Sibiu':140,'Zerind':75},
        'Timisoara':{'Lugoj':111,'Arad':118},
        'Lugoj':{'Timisoara':111,'Mehadia':70},
        'Mehadia':{'Lugoj':70,'Drobeta':75},
        'Drobeta':{'Mehadia':75,'Craiova':120},
        'Craiova':{'Drobeta':120,'Pitesti':138,'Riminicu Vilcea':146},
        'Pitesti':{'Craiova':138,'Bucharest':101,'Riminicu Vilcea':97},
        'Riminicu Vilcea':{'Pitesti':97,'Craiova':146,'Sibiu':80},
        'Sibiu':{'Riminicu Vilcea':80,'Arad':140,'Fagaras':99,'Oradea':151},
        'Fagaras':{'Sibiu':99,'Bucharest':211},
        'Bucharest':{'Fagaras':211,'Giurgiu':90,'Pitesti':101,'Urzieeni':85},
        'Hirsova':{'Urzieeni':98,'Eforie':86},
        'Urzieeni':{'Bucharest':85,'Hirsova':98,'Vaslui':142},
        'Vaslui':{'Urzieeni':142,'Iasi':92},
        'Iasi':{'Vaslui':92,'Neamt':87},
        'Neamt':{'Iasi':87},
        'Eforie':{'Hirsova':86},
        'Giurgiu':{'Bucharest':90}}

fwgraph={
    'a':{'c':-2},
    'b':{'a':4,'c':3},
    'c':{'d':2},
    'd':{'b':-1}
}
fwgraph1={
    'a':0,
    'b':1,
    'c':2,
    'd':3
}
fwgraph2={
    'Oradea':0,
    'Zerind':1,
    'Arad':2,
    'Timisoara':3,
    'Lugoj':4,
    'Mehadia':5,
    'Drobeta':6,
    'Craiova':7,
    'Pitesti':8,
    'Riminicu Vilcea':9,
    'Sibiu':10,
    'Fagaras':11,
    'Bucharest':12,
    'Urzieeni':13,
    'Hirsova':14,
    'Vaslui':15,
    'Iasi':16,
    'Neamt':17,
    'Eforie':18,
    'Giurgiu':19
    }

def dijkstras_algorithm(graph, start_city, final_city):
    closest = {}
    previous = {}
    unvisited = graph
    infinity = float("inf")
    path = []
    for vertex in unvisited:
        closest[vertex] = infinity
    closest[start_city] = 0

    while unvisited:
        closestCity = None
        for vertex in unvisited:
            if closestCity is None:
                closestCity = vertex
                #print(closestCity)

            elif closest[vertex] < closest[closestCity]:
                closestCity = vertex

        #unique vals in all potential paths in dict
        for potential_city, weight in graph[closestCity].items():
            #print(potential_city)
            if weight + closest[closestCity] < closest[potential_city]:
                closest[potential_city] = weight + closest[closestCity]
                previous[potential_city] = closestCity
                #print(potential_city)
        unvisited.pop(closestCity)

    reversePath = final_city
    while reversePath != start_city:
        path.insert(0,reversePath)
        reversePath = previous[reversePath]
    print("Task 1: The fastest path is: : " + str(closest[final_city]))
    print("Task 2: The path is: " + str(path))

def astar_search_algorithm(graph, start_city, final_city):
    closest = {}
    previous = {}
    unvisited = graph
    infinity = float("inf")
    path = []
    for vertex in unvisited:
        closest[vertex] = infinity
    closest[start_city] = 0

    while unvisited:
        closestCity = None
        for vertex in unvisited:
            if closestCity is None:
                closestCity = vertex
                #print(closestCity)

            elif closest[vertex] < closest[closestCity]:
                closestCity = vertex

        #unique vals in all potential paths in dict
        for potential_city, weight in graph[closestCity].items():
            #print(potential_city)
            if weight + closest[closestCity] < closest[potential_city]:
                closest[potential_city] = weight + closest[closestCity]
                previous[potential_city] = closestCity
                #print(potential_city)
        unvisited.pop(closestCity)

    reversePath = final_city
    while reversePath != start_city:
        path.insert(0,reversePath)
        reversePath = previous[reversePath]


def printmat(mat,nodes):
    tmp = ' '.join([str(elem) for elem in nodes])
    print('\t' + tmp)
    for i in range(len(mat)):
        tmp = str(nodes[i]) +" "+ str(mat[i])
        print(tmp)
    print("\n")

def floyd_warshall_algorithm(graph, indexed_graph, start_city, final_city):
    a = indexed_graph.get(start_city)
    b = indexed_graph.get(final_city)
    #print(b)
    vertices = 0
    the_graph = graph
    infinity = float("inf")
    nodes = list(graph.keys())
    w = len(nodes)
    h = w
    matrix = [[infinity for x in range(w)] for y in range(h)] 
    #print(matrix)
    for vertex in the_graph:
        vertices = vertices + 1
        #print(vertices)
    for v in range(vertices):
        matrix[v][v] = 0
        #print(matrix)
    for u in nodes:
        
        j = the_graph.get(u)
        #print(j)
        for i in nodes:
            if j.get(i) != None:
                matrix[int(indexed_graph.get(u))][int(indexed_graph.get(i))] = j.get(i)
                #printmat(matrix)
            #print("\n")
    #temp=matrix[a][b]
    #print(temp)
    for k in range(w):
        for i in range(h):
            for j in range(h):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    #if(matrix[a][b] != temp):
                        #temp = matrix[a][b]
                        #print(matrix[a][b])
                        #expmle = indexed_graph.get(i)
                        #print(expmle)
        #print(u)
    #    for j in u[1]:
    #        matrix[u[0]][j[1][0]] = u[1][1]
    #print(nodes)
    #printmat(matrix,nodes)
    #print(matrix)
    #print(b)
    print("Task 6 & 7: According to the Floyd Warshall Algorithm the smallest weight path between " + start_city + " and " + final_city + " is " + str(matrix[a][b]) + ".")

dijkstras_algorithm(graph, 'Arad', 'Bucharest')
#task 1 and 2
print("Task 3: A nontrivial heuristic function would be the distance between each vertex and the final city and assigning that weight to the node to base calculation on instead of automatically assigning all vertexes to infinity by default. for i in nodes: h(node)= sqrt{(x_final_city - x_i)^2 + (y_final_city-y_i)^2}")
#astar_search_algorithm(graph, start_city, final_city):

floyd_warshall_algorithm(graph2, fwgraph2, 'Arad', 'Bucharest')
#task 6 and 7 handled in func
#task 8 bonus
print("Task 9: With 20 vertices and 23 edges Dijkstra's shortest path algorithm is: O(23log20) = 29.9236899003 and Floyd Warshall is: O(20^3) = 8000. This means that Floyd Warshall is the worse algorithm out of these two. The best algorithm is either dijkstras or A* search. A* search should be better than dijkstra because the heuristic will penalize nodes that are further away from the goal. IE it will penalize taking a shorter path if it means you ultimately moved further from your end goal. Dijkstra will also use more computing power.")