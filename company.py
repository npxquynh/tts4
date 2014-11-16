class Company():
    emails = []
    emails_full = []
    roles = dict()
    names = []
    hubs = []
    auths = []
    top_candidates = dict()
    pageranks = []
    centralities = []

    def __init__(self, roles_filename):
        self.create_employee(roles_filename)

    def create_employee(self, roles_filename):
        with open(roles_filename) as f:
            for line in f:
                items = self.parse_line(line.strip())
                email = items[0]
                name = items[1]
                role = items[2]
                self.emails.append(email)
                self.names.append(name)
                self.roles[email] = role

    def parse_line(self, line):
        items = line.split("\t")
        if len(items) < 3:
            items.append("")
        return items

    def best_hub(self, filename):
        self.read_top_score(filename, "hub")

    def best_auth(self, filename):
        self.read_top_score(filename, "auth")

    def best_pagerank(self, filename):
        self.read_top_score(filename, "pagerank")

    def best_centrality(self, filename):
        self.read_top_score(filename, "centrality")        

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
                elif type == "centrality":
                    self.centralities.append(email)

    def get_intersection(self):
        self.top_candidates["hub"] = set(self.hubs).intersection(set(self.emails))
        self.top_candidates["auth"] = set(self.auths).intersection(set(self.emails))
        self.top_candidates["pagerank"] = set(self.pageranks).intersection(set(self.emails))
        self.top_candidates["centrality"] = set(self.centralities).intersection(set(self.emails))

    def print_top_candidates(self):
        for (key, candidates) in self.top_candidates.iteritems():
            print "************** %s ****************" % key
            
            count = 0
            for candiate in candidates:
                count += 1
                print("%d - %s - %s" % (count, candiate, self.roles[candiate]))

    def get_top_candidates(self):
        result = set()
        for key in self.top_candidates.keys():
            for val in self.top_candidates[key]:
                result.add(val + "@enron.com")

        return list(result)

    def print_roles(self, top_can_list):
        for can in top_can_list:
            email = can.split("@")[0]
            print "%s - %s" % (email, self.roles[email])

    def get_role(self, email):
        email = email.split("@")[0]
        return self.roles[email]
