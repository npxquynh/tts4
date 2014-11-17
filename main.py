from input import *
from map import *
from graph import *
from page_rank import *
from hits import *
from visualization import *
from company import *
from message import *
from output import *
from subject import *

import pdb

def write_graph(file, data):
    with open(file, 'w') as output:
        for doc in data:
            output.write(" ".join(doc))
            output.write("\n")

def write_result(file_name, result_list):
    with open(file_name, 'w') as output:
        for result in result_list:
            output.write("%f %s\n" % (result[0], result[1])
)
def task_1():
    INPUT_FILE = "./graph.txt"
    # INPUT_FILE = "./small_graph.txt"

    input = Input(INPUT_FILE)
    docs = input.read_file()

    map = Map()
    encoded_docs = map.create_map(docs)

    graph = Graph(encoded_docs, map.total_element())

    #########################
    # PAGE RANK
    #########################
    LAMBDA = 0.8
    page_rank = PageRank(graph, LAMBDA)

    # get top page_rank node
    result = map.get_result_from_score(page_rank.current_pr)
    write_result('pr.txt', result)

    #########################
    # HITS
    #########################
    hits = Hits(graph)

    result = map.get_result_from_score(hits.hub_scores)
    write_result('hubs.txt', result)

    result = map.get_result_from_score(hits.auth_scores)
    write_result('auth.txt', result)

def task_2(file="./pgraph.txt"):
    INPUT_FILE = file;
    # INPUT_FILE = "./small_graph.txt"

    input = Input(INPUT_FILE)
    docs = input.read_file()

    map = Map()
    encoded_docs = map.create_map(docs)

    graph = Graph(encoded_docs, map.total_element())
    graph.output_graph_info()

    #########################
    # PAGE RANK
    #########################
    # LAMBDA = 0.8
    # page_rank = PageRank(graph, LAMBDA)

    # # get top page_rank node
    # result = map.get_result_from_score(page_rank.current_pr)
    # write_result('pr_2.txt', result)

    # #########################
    # # HITS
    # #########################
    # hits = Hits(graph)

    # result = map.get_result_from_score(hits.hub_scores)
    # write_result('hubs_2.txt', result)

    # result = map.get_result_from_score(hits.auth_scores)
    # write_result('auth_2.txt', result)

    # result = map.get_result_from_score(hits.centrality_scores)
    # write_result('centrality_2.txt', result)

    return map, graph

if __name__ == "__main__":
    # task_1()
    map, graph = task_2("./pgraph.txt")

    ##########################
    # VISUALIZATION
    ##########################
    ROLES_FILE = "./roles.txt"
    company = Company(ROLES_FILE)
    company.best_hub("./hubs_2.txt")
    company.best_auth("./auth_2.txt")
    company.best_pagerank("./pr_2.txt")
    company.best_centrality("./centrality_2.txt")
    company.get_intersection()
    company.print_top_candidates()

    top_can = company.get_top_candidates()

    subject = Subject("./subject.txt")
    subject.calculate_idf()

    vis = Visualization(company, company.get_top_candidates(), graph, map, subject)
    vis.create_visualization()
    vis.get_top_count()
    vis.visualize()

    # company.print_roles(vis.top_result)
    # vis.print_analysis()

    ##########################
    # ANALYSIS
    ##########################
    # message = Message()
    # message.create_message(docs)
    # meaningful_docs = message.extract_meaningful_message(4, docs)
    # write_graph("pgraph.txt", meaningful_docs)
    # message.analyze()

    pdb.set_trace()
    a = 2
