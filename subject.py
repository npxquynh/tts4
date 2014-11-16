import re
import os
from idf import *

import pdb

class Subject():
    ids_map = dict()
    subjects = []
    idf = dict()

    def __init__(self, filename):
        with open(filename) as f:
            count = 0

            for line in f:                
                regex = '[ ]{2,}'
                items = re.split(regex, line.strip())
                if len(items) == 2:
                    self.ids_map[items[0]] = count
                    count += 1

                    # pre-process line
                    regex = "[\W]+"
                    subject = re.split(regex, items[1].lower())
                    self.subjects.append(subject)

    def calculate_idf(self):
        DEFAULT_FILE = "subject_idf.txt"

        if os.path.isfile(DEFAULT_FILE):
            with open(DEFAULT_FILE) as f:
                for line in f:
                    items = line.strip().split()
                    term = items[0]
                    value = float(items[1])
                    self.idf[term] = value
        
        if len(self.idf) == 0:
            self.idf = calculate_idf(self.subjects)
            # remove some idf
            tokens_to_remove = ["re", "fw"]
            try:
                for token in tokens_to_remove:
                    self.idf.pop(token)
            except KeyError:
                pass

            # write idf
            with open(DEFAULT_FILE, 'w') as output:
                for (key, value) in self.idf.iteritems():
                    output.write("%s %f\n" % (key, value))

    def get_subject_for(self, message_id):
        try:
            return self.subjects[self.ids_map[message_id]]
        except KeyError:
            return []

    def get_idf_for(self, token):
        try:
            return self.idf[token]
        except KeyError:
            return 0

    def calculate_tag_cloud(self, ids_list):
        score_for_token = dict()

        for message_id in ids_list:
            subject = self.get_subject_for(message_id)

            for token in subject:
                if token not in score_for_token:
                    score_for_token[token] = 0
                score_for_token[token] += self.get_idf_for(token)

        return score_for_token


