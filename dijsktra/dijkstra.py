import math
from graph import Graph ,Node


class Node:
    def __init__(self, value, neighbors=None):
        self.value = value
        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors

    def has_neighbors(self):
        if len(self.neighbors) == 0:
            return False
        return True

    def number_of_neighbors(self):
        return len(self.neighbors)

    def add_neighboor(self, neighboor):
        self.neighbors.append(neighboor)

    def __eq__(self, other):
        return self.value == other

    def __str__(self):
        returned_string = f"{self.value} -> "
        if self.has_neighbors():
            for neighboor in self.neighbors:
                returned_string += f"{neighboor[0].value} -> "

        returned_string += "None"
        return returned_string
class Graph:
    def __init__(self, nodes=None):
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes
    def add_node(self, node):
        self.nodes.append(node)
    def find_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        return None
    def add_edge(self, value1, value2, weight=1):
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)

        if (node1 is not None) and (node2 is not None):
            node1.add_neighboor((node2, weight))
            node2.add_neighboor((node1, weight))
        else:
            print("Error: One or more nodes were not found")


    def number_of_nodes(self):
        return f"The graph has {len(self.nodes)} nodes"


    def are_connected(self, node_one, node_two):
        node_one = self.find_node(node_one)
        node_two = self.find_node(node_two)

        for neighboor in node_one.neighbors:
            if neighboor[0].value == node_two.value:
                return True
        return False

    def __str__(self):
        graph = ""
        for node in self.nodes:
            graph += f"{node.__str__()}\n"
        return graph

class Vertex(Node):
    def __init__(self, value, neighbors=None):
        super().__init__(value, neighbors)
        self.length_from_start = math.inf
        self.previous_node = None
        self.visited = False

    def d1ance_from_neighbor(self, node):
        for neighbor in self.neighbors:
            if neighbor[0].value == node.value:
                return neighbor[1]
        return None

    def __str__(self):
        return f"{self.value}{self.length_from_start}{self.previous_node}{self.visited}"


class Dijkstra:
    def __init__(self, graph, start, target):
        self.graph = graph
        self.start = start
        self.target = target
        self.intialization()

    def intialization(self):
        for node in self.graph.nodes:
            if node == self.start:
                node.length_from_start = 0

    def minimum_d1ance(self):
        next_node = None
        min_value = math.inf
        for node in self.graph.nodes:
            if node.length_from_start < min_value and node.visited == False:
                min_value = node.length_from_start
                next_node = node

        return next_node

    def execution(self):
        target_node = self.graph.find_node(self.target)
        while not target_node.visited:
            selected_node = self.minimum_d1ance()
            selected_node.visited = True
            for node in selected_node.neighbors:
                connected_node = self.graph.find_node(node[0])

                if (selected_node.length_from_start + node[1]) < connected_node.length_from_start:
                    connected_node.length_from_start = selected_node.length_from_start + node[1]
                    connected_node.previous_node = selected_node.value

        path = [target_node.value]
        while True:
            node = self.graph.find_node(path[-1])
            if node.previous_node is None:
                break
            path.append(node.previous_node)

        path.reverse()
        return path, target_node.length_from_start

def main():
    # Create graph
    graph = Graph()
    # düğüm ekle
    graph.add_node(Vertex('1'))
    graph.add_node(Vertex('2'))
    graph.add_node(Vertex('3'))
    graph.add_node(Vertex('4'))
    graph.add_node(Vertex('5'))
    graph.add_node(Vertex('6'))
    graph.add_node(Vertex('7'))
    graph.add_node(Vertex('8'))
    graph.add_node(Vertex('9'))
    graph.add_node(Vertex('0'))
    # düğümler arası mesafe
    graph.add_edge('1', '3', 45)
    graph.add_edge('1', '4', 15)
    graph.add_edge('2', '3', 40)
    graph.add_edge('3', '1', 4)
    graph.add_edge('3', '2', 43)
    graph.add_edge('3', '4', 38)
    graph.add_edge('3', '6', 31)
    graph.add_edge('3', '7', 22)
    graph.add_edge('3', '0', 11)
    graph.add_edge('4', '1', 14)
    graph.add_edge('4', '3', 38)
    graph.add_edge('4', '5', 34)
    graph.add_edge('4', '6', 13)
    graph.add_edge('5', '4', 35)
    graph.add_edge('5', '6', 35)
    graph.add_edge('5', '8', 40)
    graph.add_edge('6', '3', 9)
    graph.add_edge('6', '4', 13)
    graph.add_edge('6', '5', 35)
    graph.add_edge('7', '3', 2)
    graph.add_edge('7', '9', 35)
    graph.add_edge('8', '5', 48)
    graph.add_edge('8', '9', 69)
    graph.add_edge('9', '7', 34)
    graph.add_edge('9', '8', 61)
    graph.add_edge('9', '0', 52)
    graph.add_edge('0', '3', 10)
    graph.add_edge('0', '9', 23)
    #algoritmayı çalıştır
    alg = Dijkstra(graph, "1", "7")
    path, path_lenght = alg.execution()
    print(" -> ".join(path))
    print(f"Kan Bankası ile Hastane Arasındaki En Kısa Yol(km): {path_lenght}")
if __name__ == '__main__':
    main()