import numpy
from graphviz import Graph as GraphV

import pdb

class Visualization():
    emails = []
    count = None

    def __init__(self, company, emails, graph, map, subject):
        self.company = company
        self.emails = emails
        self.graph = graph
        self.map = map
        self.subject = subject

        a = 2

    def create_visualization(self):
        l = len(self.emails)
        self.count = [[0 for i in range(l)] for i in range(l)]

        for i in range(l - 1):
            id_1 = self.map.get_pos_from(self.emails[i])
            for j in range(1, l):
                id_2 = self.map.get_pos_from(self.emails[j])

                self.set_count(i, j, self.graph.count_message_from_to(id_1, id_2))

    def set_count(self, i, j, val):
        self.count[i][j] = val

    def print_analysis(self):
        row_sum = numpy.sum(self.count, 1)
        for i in range(len(row_sum)):
            print row_sum[i]

        col_sum = numpy.sum(self.count, 0)
        for i in range(len(col_sum)):
            print col_sum[i]

        for i in range(len(self.emails)):
            print self.emails[i]

    def get_top_count(self):
        top_result = set()
        cutoff = 100

        l = len(self.emails)
        for i in range(l):
            for j in range(l):
                if self.count[i][j] >= 100:
                    top_result.add(self.emails[i])
                    top_result.add(self.emails[j])

        # filtered by role
        refined_top_result = []

        priority_role = ["CEO", "President", "Vice President", "Manager", "Managing Director"]
        # priority_role = ["CEO", "President", "Vice President", "Manager", "Employee", "Managing Director"]
        for result in top_result:
            role = self.company.get_role(result)
            if role in priority_role:
                refined_top_result.append(result)

        self.top_result = refined_top_result

    def get_message_list_between(self, email_1, email_2):
        id_1 = self.map.get_pos_from(email_1)
        id_2 = id_2 = self.map.get_pos_from(email_2)

        message_list = self.graph.get_message_id_from_to(id_1, id_2)
        message_list = message_list + self.graph.get_message_id_from_to(id_2, id_1)

        return message_list

    def get_top_tag_cloud(self, tags, cutoff = 10):
        keys = tags.keys()
        values = tags.values()

        sorted_indices = [i[0] for i in sorted(enumerate(values), reverse=True, key = lambda x:x[1])]

        top_tag = []
        l = min(cutoff, len(sorted_indices))

        # pdb.set_trace()
        for i in range(1, l):
            try:
                top_tag.append(keys[sorted_indices[i]])
            except IndexError:
                pdb.set_trace()

            # top_tag.append(keys[sorted_indices[i]])

        return top_tag

    def visualize(self):
        l = len(self.top_result)

        connections = dict()
        tags = dict()

        for i in range(l - 1):
            for j in range(1, l):
                if i != j:
                    key = (i, j)

                    message_list = self.get_message_list_between(self.top_result[i], self.top_result[j])
                    tag_cloud = self.subject.calculate_tag_cloud(message_list)

                    tags[key] = self.get_top_tag_cloud(tag_cloud, 5)

        # DOT language
        dot = GraphV(comment = "Information Flow - Enron")
        for i in range(l):
            dot.node(str(i), self.top_result[i] + " - " + self.company.get_role(self.top_result[i]))

        for (edge, tag) in tags.iteritems():
            node_1 = edge[0]
            node_2 = edge[1]
            note = ", ".join(tag)
            print note
            dot.edge(str(node_1), str(node_2), label=note)


        dot.render('test-output/round-table.gv', view=False)