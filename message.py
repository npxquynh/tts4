class Message():
    def __init__(self):
        self.N = 0
        self.ids = dict()

    def create_message(self, docs):
        self.N = len(docs)

        for [_id, email_1, email_2] in docs:
            if _id not in self.ids:
                self.ids[_id] = 0;

            if email_1 != email_2:
                self.ids[_id] += 1

    def analyze(self):
        print "Total messages: %d" % self.N
        print "Total distinct messages: %d" % len(self.ids)
        for i in range(1, 20):
            print "Distinct message with <= recipients - %d \t %d" % (i, self.count_message_to_n_recipients(i))

        for i in range(1,20):
            print self.count_message_to_n_recipients(i) * 100.0 / len(self.ids)

    def extract_meaningful_message(self, cutoff, docs):
        meaningful_docs = []
        for [_id, email_1, email_2] in docs:
            if self.count_id(_id) <= cutoff:
                if email_1 != email_2:
                    meaningful_docs.append([_id, email_1, email_2])

        return meaningful_docs         

    def count_id(self, _id):
        try:
            return self.ids[_id]
        except KeyError:
            return 0

    def count_message_to_n_recipients(self, n):
        count_array = self.ids.values()
        s = 0
        for val in count_array:
            if val <= n:
                s += 1

        return s

