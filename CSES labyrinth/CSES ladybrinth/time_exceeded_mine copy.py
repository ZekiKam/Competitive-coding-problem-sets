#Create graph
from collections import deque

graph = []

n,m = input().split(' ')
n = int(n)
m = int(m)
a = ()
b = ()

for i in range(n):
    graph.append(input())
#print(graph)

for y in range(0, n): #height
    for x in range(0, m): #width
    #graph[height][width] so we have use this arrangement to access elements in graph throughout the program (i.e. graph[y][x])
        if graph[y][x] == 'A':
            a = (y,x)
        elif graph[y][x] == 'B':
            b = (y,x)

#Use BFS
#Use dictionary for visited to store node visited
visited = {}
queue = deque()
moves = {}

#Adjacents = left, right, up, down
#in the form [j,i,move]
directions = [[0,-1,'L'],[0,1,'R'],[-1,0,'U'],[1,0,'D']]

#A is root node, so pass A as argument
def bfs(graph,node):
    #Set root (A) as current node
    current = node
    queue.append(current)
    #so we can start with dequeuing A
    arrived = False

    '''Since BFS explores layer by layer, when B is reached
    for the first time, the path must be shortest, as other paths
    would require traversing to deeper layers'''

    while queue:# and arrived == "NO":
        current = queue.popleft()

        '''
        print("Current queue:",queue)
        print("Current visited:",visited.keys())
        print("Current parent:",visited.values())
        print("Current node:",current)
        '''

        for j,i,move in directions:
            #Flag this point if it has > 1 adjacent dots, cuz we might need to backtrack
            #Check adjacents nodes of current nodes
            y = current[0] + j
            x = current[1] + i
            adj = (y,x)
            #print(adj)

            #Check if we have arrived B
            if adj == b:
                arrived = True
                visited[adj] = current
                moves[adj] = move
                return arrived

            if (0 <= y < n and 0 <= x < m) and graph[y][x] == "." and adj not in visited:
                visited[adj] = current
                queue.append(adj)
                moves[adj] = move

    #If path not found
    return arrived

    '''Now that we have found B, we need to backtrack to find
    the shortest path using prev nodes, as some nodes in visited
    aren't involved in the shortest path'''

#Backtrack to construct route, starting from B
if bfs(graph,a):
    route = []
    node = b
    #print(node)
    while node != a:
        route.append(moves[node])
        node = visited[node]
    route.reverse()
    print("YES")
    print(len(route))
    print(''.join(route))
else:
    print("NO")

'''
10 10
##.A######
#.##.##.##
#####..###
.#########
.########.
###.###.##
#########.
######.#.#
###..###.#
###.B#####

5 8
########
#.A#...#
#.##.#B#
#......#
########
'''


