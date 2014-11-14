import pdb

class Graph():
    def __init__(self, edges, N):
        self.N = 0
        self.E = 0

        print "1st attempt total_nodes = %d" % N

        # should we use just a simple data structure, or should I get more complex data structure to store node???
        self.nodes = []
        self.incoming = dict()
        self.outgoing = dict()
        self.same_edges = dict()
        self.add_edges(edges)

        self.analyze()

    def add_edges(self, edges):
        for [node_1, node_2] in edges:
            self.E += 1

            if node_1 == node_2:
                if node_1 not in self.same_edges:
                    self.same_edges[node_1] = 0
                self.same_edges[node_1] += 1
            else:
                if node_1 not in self.outgoing:
                    self.outgoing[node_1] = [node_2]
                else:
                    self.outgoing[node_1].append(node_2)

                if node_2 not in self.incoming:
                    self.incoming[node_2] = [node_1]
                else:
                    self.incoming[node_2].append(node_1)

        # update self.N
        nodes_set = set(self.incoming.keys()).union(set(self.outgoing.keys()))
        self.N = len(nodes_set)
        self.nodes = list(nodes_set)

    def analyze(self):
        self.sink_nodes = []

        nodes = self.incoming.keys()

        for node in nodes:
            if node not in self.outgoing:
                self.sink_nodes.append(node)

    def output_graph_info(self):
        print("self.N: %d" % self.N)
        print("self.E: %d\n" % self.E)
        print("outgoing: %d" % len(self.outgoing))
        print("# outgoing: %d\n" % self.count_outgoing())
        print("incoming: %d" % len(self.incoming))
        print("# incoming: %d\n" % self.count_incoming())
        print("same: %d" % len(self.same_edges))
        print("# same email: %d\n" % sum(self.same_edges.values()))
        print("sink nodes: %d" % len(self.sink_nodes))
        print("sink nodes = %s" % self.sink_nodes)

    def get_sink_nodes(self):
        return self.sink_nodes

    def count_sink_nodes(self):
        return len(self.sink_nodes)

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

    def count_outgoing(self):
        return sum([len(i) for i in self.outgoing.values()])

    def count_incoming(self):
        return sum([len(i) for i in self.incoming.values()])