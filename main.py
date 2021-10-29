#import dependencies
import pandas as pd
import numpy as np

#read data
df = pd.read_csv("Data/dummy.csv", header = None, names = ["Name", "Email", "Restricted Members"])

class Edge:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient

class Person:
    def __init__(self, name, email, edges):
        self.name = name
        self.email = email
        self.edges = edges
        self.hash = 0
    
    #Takes a person's name and converts it into a number
    def obfuscate(name):
        pass

    #Takes a number and tries to insert it into a hash table using a rolling hash
    def rollingHash(number):
        pass

    #Takes a hash and tries to return the number 

class Graph:
    def __init__(self, n):
        #adjacency matrix representation of a graph
        #inititialized with all 1 representing a fully connected graph
        self.adj_matrix = [[1 for c in range(n)] for r in range(n)]
        
        #Number of participants
        self.vertices = n

    #cheks if the vertex being considered is a legal vertex
    def isValid(self, vertex, index, path):
        #make sure there is an edge between last vertex and considered vertex
        if self.adj_matrix[path[index - 1] - 1] [vertex - 1] == 0:
            return False
        #make sure the vertex being considered isn't alredy in the path
        for v in path:
            if v == vertex: 
                return False
        #else return True
        return True
    
    #Recursive algorithm to find Hamiltonian Path
    def findHam(self, path, pos):
        #traversed all of the verticies
        if pos == self.vertices:
            #Does the last vertex connect to vertex 1?
            if self.adj_matrix[path[pos - 1] - 1][path[0] - 1] == 1:
                return True
                
            else:
                return False

        #our starting point is vertex 1 so we start at vertex 2 and we want
        # to try every vertex (eventually) for a solution 
        for v in range(1 , self.vertices + 1):
            #if the vertex is valid then we add it to the path
            if self.isValid(v, pos, path) == True:
                path[pos] = v
                #we continue to recurse 
                if self.findHam(path, pos + 1) == True:
                    return True
                #if the current vertex doesn't have any possible paths
                path[pos] = 0

        return False

    def solver(self):
        #initialize the path list 
        path = [0] * self.vertices
        #start with vertex 1
        path[0] = 1

        #no solution exists
        if self.findHam(path, 1) == False:
            print("There is no Hamiltonian Cycle")
            return False

        print(path)
        return True

g1 = Graph(4)
g1.solver()

g1.adj_matrix= np.array(
            [[0, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 0]])
g1.solver()

g1.adj_matrix= np.array(
            [[0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]])
g1.solver()