import math

def calculate_idf(docs):
    N = len(docs) * 1.0

    # Calculate df
    df = dict()
    for doc in docs:
        for token in set(doc):
            if token not in df:
                df[token] = 0

            df[token] += 1

    idf = dict()
    # Calculate idf
    for (key, value) in df.iteritems():
        idf[key] = math.log(N/value)

    if " " in idf:
        idf.pop(" ")
    if "" in idf:
        idf.pop("")

    return idf