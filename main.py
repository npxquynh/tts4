from input import *
from map import *
from graph import *
from page_rank import *
from hits import *

import pdb

def write_result(file_name, result_list):
    with open(file_name, 'w') as output:
        for result in result_list:
            output.write("%f %s\n" % (result[0], result[1]))

def get_result_from_score(score_list):
    sorted_indices = [i[0] for i in sorted(enumerate(score_list), reverse=True, key = lambda x:x[1])]

    result = list()
    for i in range(min(100, len(score_list))):
        node_id = sorted_indices[i]
        pr = score_list[node_id]
        email = map.get_email_from(node_id)
        result.append((pr, email))

    return result

if __name__ == "__main__":
    INPUT_FILE = "./small_graph.txt"

    input = Input(INPUT_FILE)
    docs = input.read_file()

    map = Map()
    encoded_docs = map.create_map(docs)

    graph = Graph(encoded_docs, map.total_element())

    ##########################
    # PAGE RANK
    ##########################
    LAMBDA = 0.8
    page_rank = PageRank(graph, LAMBDA)

    # get top page_rank node
    result = get_result_from_score(page_rank.current_pr)
    write_result('pr.txt', result)

    ##########################
    # HITS
    ##########################
    hits = Hits(graph)

    result = get_result_from_score(hits.hub_scores)
    write_result('hubs.txt', result)

    result = get_result_from_score(hits.auth_scores)
    write_result('auth.txt', result)