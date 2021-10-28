#import dependencies
import pandas as pd

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
        self.adj_matrix = [[1 for c in range(n)] for r in range(n)]

#def findCycle()
