class Node:
    """
    Class Node
    """
    def fun(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    """
    Class tree will provide a tree as well as utility functions.
    """

    def createNode(self, data):
        """
        Utility function to create a node.
        """
        return Node(data)

    def insert(self, node , data):
        """
        Insert function will insert a node into tree.
        Duplicate keys are not allowed.
        """
        #if tree is empty , return a root node
        if node is None:
            return self.createNode(data)
        # if data is smaller than parent , insert it into left side
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)

        return node


    def search(self, node, data):
        """
        Search function will search a node into tree.
        """
        # if root is None or root is the search data.
        if node is None or node.data == data:
            return node

        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)



    def deleteNode(self,node,data):
        """
        Delete function will delete a node into tree.
        Not complete , may need some more scenarion that we can handle
        Now it is handling only leaf.
        """

        # Check if tree is empty.
        if node is None:
            return None

        # searching key into BST.
        if data < node.data:
            node.left = self.deleteNode(node.left, data)
        elif data > node.data:
            node.right = self.deleteNode(node.right, data)
        else: # reach to the node that need to delete from BST.
            if node.left is None and node.right is None:
                del node
            if node.left == None:
                temp = node.right
                del node
                return  temp
            elif node.right == None:
                temp = node.left
                del node
                return temp

        return node

    def traverseInorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traverseInorder(root.left)
            print(root.data)
            self.traverseInorder(root.right)

    def traversePreorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            print(root.data)
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)

    def traversePostorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traversePostorder(root.left)
            self.traversePostorder(root.right)
            print(root.data)


  
# A class to represent the adjacency list of the node 

class AdjNode: 

    def __init__(self, data): 

        self.vertex = data 

        self.next = None

  

  
# A class to represent a graph. A graph 
# is the list of the adjacency lists. 
# Size of the array will be the no. of the 
# vertices "V" 

class Graph: 

    def __init__(self, vertices): 

        self.V = vertices 

        self.graph = [None] * self.V 

  

    # Function to add an edge in an undirected graph 

    def add_edge(self, src, dest): 

        # Adding the node to the source node 

        node = AdjNode(dest) 

        node.next = self.graph[src] 

        self.graph[src] = node 

  

        # Adding the source node to the destination as 

        # it is the undirected graph 

        node = AdjNode(src) 

        node.next = self.graph[dest] 

        self.graph[dest] = node 

  

    # Function to print the graph 

    def print_graph(self): 

        for i in range(self.V): 

            print("Adjacency list of vertex {}\n head".format(i), end="") 

            temp = self.graph[i] 

            while temp: 

                print(" -> {}".format(temp.vertex), end="") 

                temp = temp.next

            print(" \n") 

  

  
# Driver program to the above graph class 



   



def main():
    root = None
    tree = Tree()
    root = tree.insert(root, 10)
    print(root)
    tree.insert(root, 20)
    tree.insert(root, 30)
    tree.insert(root, 40)
    tree.insert(root, 70)
    tree.insert(root, 60)
    tree.insert(root, 80)

    print("Traverse Inorder")
    tree.traverseInorder(root)

    print("Traverse Preorder")
    tree.traversePreorder(root)

    print("Traverse Postorder")
    tree.traversePostorder(root)

    V = 5

    graph = Graph(V) 

    graph.add_edge(0, 1) 

    graph.add_edge(0, 4) 

    graph.add_edge(1, 2) 

    graph.add_edge(1, 3) 

    graph.add_edge(1, 4) 

    graph.add_edge(2, 3) 

    graph.add_edge(3, 4) 

  

    graph.print_graph()


if __name__ == "__main__":
    main()

