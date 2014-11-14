import numpy

class Hits():
    def __init__(self, graph):
        self.graph = graph
        self.N = self.graph.N
        one_over_sqrt_N = 1.0 / pow(self.N, 0.5)

        self.hub_scores = [one_over_sqrt_N for i in range(self.N)]
        self.auth_scores = [one_over_sqrt_N for i in range(self.N)]

        self.new_hub_scores = [0 for i in range(self.N)]
        self.new_auth_scores = [0 for i in range(self.N)]

        self.iterate()

    def iterate(self):
        count = 0
        while (count < 10):
            count += 1
            print "*********** HITS %d ***********\n" % count
            self.verify()
            self.sanity_check()

            # Update Authority score
            for i in range(self.N):
                incoming_nodes = self.graph.incoming_of(i)

                new_score = 0
                for node in incoming_nodes:
                    new_score += self.get_hub_score(node)

                self.set_auth_score(i, new_score)

            self.normalize_score("auth")
            self.update_auth_score()

            # Update Hub score
            for i in range(self.N):
                outgoing_nodes = self.graph.outgoing_of(i)

                new_score = 0
                for node in outgoing_nodes:
                    new_score += self.get_auth_score(node)

                self.set_hub_score(i, new_score)

            # self.normalize_score("auth")
            # self.update_auth_score()
            self.normalize_score("hub")
            self.update_hub_score()
            # self.update_auth_score()

    def verify(self):
        a = sum(numpy.square(self.hub_scores))
        b = sum(numpy.square(self.auth_scores))
        print "Verify: %f %f\n" % (a, b)
        # print self.hub_scores
        # print self.auth_scores
        # print self.new_hub_scores
        # print self.new_auth_scores

    def sanity_check(self):
        a = 2
        # print out the value for 
        # 43 john.lavorato@enron.com
        # 51 jeff.dasovich@enron.com
        # print "Hub for 51: %f" % self.hub_scores[51]
        # print "Hub for 43: %f" % self.hub_scores[43]

        # print "Auth for 51: %f" % self.auth_scores[51]
        # print "Auth for 43: %f" % self.auth_scores[43]

    def normalize_score(self, type):
        if type == "hub":
            squared_score = numpy.square(self.new_hub_scores)
            root_sum = pow(sum(squared_score), 0.5)
            self.new_hub_scores = numpy.divide(self.new_hub_scores, root_sum)
        elif type == "auth":
            squared_score = numpy.square(self.new_auth_scores)
            root_sum = pow(sum(squared_score), 0.5)
            self.new_auth_scores = numpy.divide(self.new_auth_scores, root_sum)

    def update_hub_score(self):
        self.hub_scores = self.new_hub_scores
        self.new_hub_scores = [0 for i in range(self.N)]

    def update_auth_score(self):
        self.auth_scores = self.new_auth_scores
        self.new_auth_scores = [0 for i in range(self.N)]

    def get_hub_score(self, node_id):
        return self.hub_scores[node_id]

    def set_hub_score(self, node_id, new_score):
        self.new_hub_scores[node_id] = new_score

    def get_auth_score(self, node_id):
        return self.auth_scores[node_id]

    def set_auth_score(self, node_id, new_score):
        self.new_auth_scores[node_id] = new_score
