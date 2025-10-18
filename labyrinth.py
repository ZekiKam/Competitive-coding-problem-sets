#Problem set here: https://cses.fi/problemset/task/1193/
#Code works, but only passed 3 tests...
#Need a more memory efficient solution

#Create graph

graph = []

n,m = input().split(' ')
n = int(n)
m = int(m)
a = ()
b = ()
dots = []

for i in range(n):
    graph.append(input())
#print(graph)

for y in range(0, n-1): #height
    for x in range(0, m-1): #width
    #graph[height][width] so we have use this arrangement to access elements in graph throughout the program (i.e. graph[y][x])
        if graph[y][x] == '.':
            dots.append((y,x))
        elif graph[y][x] == 'A':
            a = (y,x)
        elif graph[y][x] == 'B':
            b = (y,x)
'''
print("A:",a)
print("B:",b)
print("Dots:",dots)
'''

#Use BFS
#Use dictionary for visited to store node visited and previous node of every node as a key-value pair
visited = {}
queue = []
moves = {}

#Adjacents = left, right, up, down
#in the form [j,i,move]
directions = [[0,-1,'L'],[0,1,'R'],[-1,0,'U'],[1,0,'D']]

#A is root node, so pass A as argument
def bfs(graph,node):
    #Set root (A) as current node
    current = node
    previous = node
    visited[current] = previous
    queue.append(current)
    #so we can start with dequeuing A
    arrived = "NO"

    '''Since BFS explores layer by layer, when B is reached
    for the first time, the path must be shortest, as other paths
    would require traversing to deeper layers'''

    while len(queue) > 0 and arrived == "NO":
        previous = current
        current = queue[0]
        '''
        print("Current queue:",queue)
        print("Current visited:",visited.keys())
        print("Current parent:",visited.values())
        print("Current node:",current)
        '''
        queue.pop(0)
        
        if current == b:
            arrived = "YES"
            visited[current] = previous
            return arrived
        
        if current not in visited.keys():
            visited[current] = previous

        for j,i,move in directions:
            #Flag this point if it has > 1 adjacent dots, cuz we might need to backtrack
            count = 0
            #Check adjacents nodes of current nodes
            y,x = (current[0] + j),(current[1] + i)
            adj = (y,x)
            #print(adj)

            #Check if we have arrived B
            if adj == b:
                arrived = "YES"
                visited[adj] = current
                moves[adj] = move
                return arrived

            if adj in dots and adj not in visited.keys():
                visited[adj] = current
                queue.append(adj)
                moves[adj] = move

    #If path not found
    return arrived

    '''Now that we have found B, we need to backtrack to find
    the shortest path using prev nodes, as some nodes in visited
    aren't involved in the shortest path'''

#Backtrack to construct route, starting from B
print(bfs(graph,a))
route = []
node = b
while node != a:
    route.append(moves[node])
    node = visited[node]
route.reverse()
print(len(route))
print(''.join(route))
