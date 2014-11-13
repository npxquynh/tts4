import pdb

class Map():
    def __init__(self):
        self.email_number = dict()
        self.number_email = []
        self.max_number = 0

    def create_map(self, docs):
        new_docs = []
        try:
            for [id, email_1, email_2] in docs:
                self.map_email_number(email_1)
                self.map_email_number(email_2)

                no_1 = self.get_pos_from(email_1)
                no_2 = self.get_pos_from(email_2)

                new_docs.append([no_1, no_2])
        except KeyError:
            print "ERROR in input format"

        return new_docs

    def map_email_number(self, email):
        if email not in self.email_number:
            self.email_number[email] = self.max_number
            self.number_email.append(email)
            self.max_number += 1

    def get_email_from(self, pos):
        return self.number_email[pos]

    def get_pos_from(self, email):
        return self.email_number[email]

    def total_element(self):
        return self.max_number
