class Company():
    emails = []
    roles = dict()
    hubs = []
    auths = []
    top_candidates = dict()
    pageranks = []

    def __init__(self, roles_filename):
        self.create_employee(roles_filename)

    def create_employee(self, roles_filename):
        with open(roles_filename) as f:
            for line in f:
                email, role = self.parse_line(line)
                self.emails.append(email)
                self.roles[email] = role

    def parse_line(self, line):
        pos = line.find("\t")
        return line[:pos], line[pos+1:]

    def best_hub(self, filename):
        self.read_top_score(filename, "hub")

    def best_auth(self, filename):
        self.read_top_score(filename, "auth")

    def best_pagerank(self, filename):
        self.read_top_score(filename, "pagerank")

    def read_top_score(self, filename, type):
        with open(filename) as f:
            for line in f:
                email = line.strip().split()[1].split("@")[0]
                if type == "hub":
                    self.hubs.append(email)
                elif type == "auth":
                    self.auths.append(email)
                elif type == "pagerank":
                    self.pageranks.append(email)

    def get_intersection(self):
        self.top_candidates["hub"] = set(self.hubs).intersection(set(self.emails))
        self.top_candidates["auth"] = set(self.auths).intersection(set(self.emails))
        self.top_candidates["pagerank"] = set(self.pageranks).intersection(set(self.emails))

    def print_top_candidates(self):
        for (key, candidates) in self.top_candidates.iteritems():
            print "************** %s ****************" % key
            
            for candiate in candidates:
                print("%s - %s" % (candiate, self.roles[candiate]))

