from input import *
from map import *
from graph import *
from page_rank import *

import pdb

if __name__ == "__main__":
    INPUT_FILE = "./small_graph.txt"

    input = Input(INPUT_FILE)
    docs = input.read_file()

    map = Map()
    encoded_docs = map.create_map(docs)

    graph = Graph(encoded_docs, map.total_element())

    LAMBDA = 0.8
    page_rank = PageRank(graph, LAMBDA)



