
##################################################################################################
############################## DIJKSTRA'S SHORTEST PATH ALGORITHM ################################
##################################################################################################

print("##################################################################################################")
print("                                DIJKSTRA'S SHORTEST PATH ALGORITHM ")
print("##################################################################################################")

############################################# INITIALIZATIONS ###################################################

import sys
INT_MAX = sys.maxsize

############################################# GRAPH CLASS ###################################################

class Graph():   

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]

    def printVertexDistFromSource(self, dist): 
        print("To Vertex\t Distance from Source")
        print("=========\t ====================")
        for node in range(self.V):
            print(node,"   \t\t",dist[node])

    def findMinDistance(self, dist, sptSet):
        minn, minn_idx = INT_MAX, 0
        for v in range(self.V):
            if sptSet[v] == False and dist[v] <= minn:
                minn, minn_idx = dist[v], v 
        
        return minn_idx

    def djkstra(self, src): 

        dist = [INT_MAX]*self.V
        sptSet = [False]*self.V

        dist[src] = 0

        for i in range(self.V):
            u = self.findMinDistance(dist,sptSet)

            sptSet[u] = True 

            for v in range(self.V):
                if ( not sptSet[v] ) and self.graph[u][v] and ( dist[u] != INT_MAX ) and ( dist[u] + self.graph[u][v] < dist[v] ) :
                    dist[v] = dist[u] + self.graph[u][v]

        self.printVertexDistFromSource(dist)


######################################### MAIN FUNCTION CODE #############################################

n = int(input("Enter No. of Nodes in the graph/ network: "))

# g = Graph(9)

# g.graph = [   
#         [ 0, 4, 0, 0, 0, 0, 0, 8, 0 ], 
#         [ 4, 0, 8, 0, 0, 0, 0, 11, 0 ], 
#         [ 0, 8, 0, 7, 0, 4, 0, 0, 2 ], 
#         [ 0, 0, 7, 0, 9, 14, 0, 0, 0 ], 
#         [ 0, 0, 0, 9, 0, 10, 0, 0, 0 ], 
#         [ 0, 0, 4, 14, 10, 0, 2, 0, 0 ], 
#         [ 0, 0, 0, 0, 0, 2, 0, 1, 6 ], 
#         [ 8, 11, 0, 0, 0, 0, 1, 0, 7 ], 
#         [ 0, 0, 2, 0, 0, 0, 6, 7, 0 ] 
#           ] 

g = Graph(n)

print("Enter the Distance values: ")
g.graph = []

for x in range(n):
    l = list(map(int,input().split()))
    g.graph.append(l)

print("Distance matrix is: ")
for i in range(n):
    print("    ",i,end=" ") if i==0 else print(i,end=" ")
print()

for i in range(2*n):
    print("- ",end="")
print()

for i in range(n):
    print(i,"->",end=" ")
    for j in range(n):
        print(g.graph[i][j], end=" ")
    print()
print()

src_node = int(input("Enter Source Node Number: "))
print()

print("ACC. TO DIJKSTRAs ALGORITHM, Minimun Distance From Source Node to all other Nodes is:\n ")
print("From Source: ",src_node)
print()

g.djkstra(src_node)


