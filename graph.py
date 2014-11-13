import pdb

class Graph():
    def __init__(self, edges, N):
        self.N = N
        self.E = len(edges)

        # should we use just a simple data structure, or should I get more complex data structure to store node???
        self.incoming = dict()
        self.outgoing = dict()
        self.add_edges(edges)

    def add_edges(self, edges):
        for [node_1, node_2] in edges:
            self.E += 1

            if node_1 not in self.outgoing:
                self.outgoing[node_1] = [node_2]
            else:
                self.outgoing[node_1].append(node_2)

            if node_2 not in self.incoming:
                self.incoming[node_2] = [node_1]
            else:
                self.incoming[node_2].append(node_1)

    def analyze(self):
        node_set = set(self.incoming.keys()).union(set(self.outgoing.keys()))
        self.N = len(node_set)

    def outgoing_of(self, node_id):
        if node_id in self.outgoing:
            return self.outgoing[node_id]
        else:
            return []

    def incoming_of(self, node_id):
        if node_id in self.incoming:
            return self.incoming[node_id]
        else:
            return []

    def count_outgoing_of(self, node_id):
        try:
            return len(self.outgoing[node_id])
        except:
            return 0

    def count_incoming_of(self, node_id):
        try:
            return len(self.incoming[node_id])
        except KeyError:
            return 0