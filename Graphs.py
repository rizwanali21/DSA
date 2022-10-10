

""" 
A python program implementing the Graph data structure using design principles 
"""

  
# A class for a node of a graph 

class Node: 

    def __init__(self, value): 

        self.vertex = value 
        self.next = None

  

  
""" A class representing a graph. A graph 
 is basically a list of the adjacency lists. 
 Size of the list will be the number of the 
 vertices "V" """

class Graph: 

    def __init__(self, vertices): 

        self.V = vertices 

        self.graph = [None] * self.V 

  

    """undefined function which will be implemented by
        child classes accordingly
    """ 

    def connectVertex(self, src, dest): 

        pass

    """
        A Search function which will be implemented by
        child classes as BFS or DFS
    """
    def Search(self):
        pass


    """
        A function to delete a vertex
        this is commonly shared by all classes
    """
    def delvertex(self, k): 

  
# Iterating through all the vertices of the graph 

        for i in range(self.v): 

            temp = self.graph[i] 

            if i == k: 

                while temp: 

                    self.graph[i]= temp.next

                    temp = self.graph[i] 

                      

            # Delete the vertex  

            # using linked list concept         

            if temp: 

                if temp.vertex == k: 

                    self.graph[i]= temp.next

                    temp = None

            while temp: 

                if temp.vertex == k: 

                    break

                prev = temp 

                temp = temp.next

  

            if temp == None: 

                continue

  

            prev.next = temp.next

            temp = None

        

    # Function to print the graph 

    def print_graph(self): 
        for i in range(self.V): 
            print("Adjacency list of vertex {}\n head".format(i), end="") 

            temp = self.graph[i] 
            while temp: 

                print(" -> {}".format(temp.vertex), end="") 

                temp = temp.next

            print(" \n") 
  

  
    """
        A class representing Undirected Graph
    """

class UndirectedGraph(Graph):
    def connectVertex(self, src, dest): 

        # Adding the node to the source node in an undirected graph

        node = Node(dest) 

        node.next = self.graph[src] 

        self.graph[src] = node 

  

        # Adding the source node to the destination as 

        # it is the undirected graph 

        node = Node(src) 

        node.next = self.graph[dest] 

        self.graph[dest] = node
    """
        A Search function which was defined by
        parent class is implemented as BFS
    """
    def Search(self):
        start=0
        end=2

        queue = []
        visited = []

        done = 'false'
        while done != 'true':
            if start == end:
                done = 'true'
                visited.append(start)
            else:
                visited.append(start)
                temp=self.graph[start]
                listing=[]
                while temp:
                    listing.append(temp.vertex)
                    temp=temp.next
                #listing = d[start]
                listing.sort()
                for i in range(0, len(listing)):
                    if listing[i] in visited or listing[i] in queue:
                        c=0
                    else:
                        queue.append(listing[i])
                if(not queue):
                    print("Path not Found!")
                else:
                    start = queue.pop(0)
        print("*******************************/n")
        print("Path Visited: ",visited)
        print("Items left in a queue",queue)
        print("*******************************/n")


    """
        A class representing Undirected Graph
    """

class DirectedGraph(Graph):
    def connectVertex(self, src, dest): 

        # Adding the node to the source node in a directed graph 

        node = Node(dest) 

        node.next = self.graph[src] 

        self.graph[src] = node 

  

    """
        A Search function which was defined by
        parent class is implemented as DFS
    """
    def Search(self):
        start=0
        end=2

        queue = []
        visited = []

        done = 'false'
        while done != 'true':
            if start == end:
                done = 'true'
                visited.append(start)
            else:
                visited.append(start)
                temp=self.graph[start]
                listing=[]
                while temp:
                    listing.append(temp.vertex)
                    temp=temp.next
                #listing = d[start]
                listing.sort()
                for i in range(0, len(listing)):
                    if listing[i] in visited or listing[i] in queue:
                        c=0
                    else:
                        queue.append(listing[i])
                if(not queue):
                    print("Path not Found!")
                else:
                    start = queue.pop(-1)
        print("*******************************/n")
        print("Path Visited: ",visited)
        print("Items left in a queue",queue)
        print("*******************************/n")

    


    



    
        



def main():

    print("**********************")
    print("Undirected Graph")
    print("**********************")
    V = 5

    graph = UndirectedGraph(V) 

    graph.connectVertex(0, 1) 

    graph.connectVertex(0, 4) 

    graph.connectVertex(1, 2) 

    graph.connectVertex(1, 3) 

    graph.connectVertex(1, 4) 

    graph.connectVertex(2, 3) 

    graph.connectVertex(3, 4) 

    graph.Search()

    print("**********************")
    print("Directed Graph")
    print("**********************")
    V = 5

    graph = DirectedGraph(V) 

    graph.connectVertex(0, 1) 

    graph.connectVertex(0, 4) 

    graph.connectVertex(1, 2) 

    graph.connectVertex(1, 3) 

    graph.connectVertex(1, 4) 

    graph.connectVertex(2, 3) 

    graph.connectVertex(3, 4) 

    graph.Search()


    

  
    


if __name__ == "__main__":
    main()
