import os.path

from src.controllers.InputFileLoader import load_input_files
from src.controllers.utilities import Logger


def filename_inquiries():
    while True:
        filename_queries = input("Please specify the queries input directory (e.g., ../datasources/queries.xml) : ")
        if filename_queries != "" and os.path.exists(filename_queries):
            Logger.log("The queries file > " + filename_queries + " exists.")
            break
        else:
            Logger.log("Unable to read the specified filename > " + filename_queries, Logger.LogLevel.ERROR)

    while True:
        filename_corpus = input("Please specify the weakness corpus input directory (e.g., ../datasources/corpus.xml) "
                                ": ")
        if filename_corpus != "" and os.path.exists(filename_corpus):
            Logger.log("The corpus file > " + filename_corpus + " exists")
            break
        else:
            Logger.log("Unable to read the specified filename > " + filename_corpus, Logger.LogLevel.ERROR)

    while True:
        filename_graph = input("Please specify the knowledge graph input directory (e.g., ../datasources/cdkg.xml) : ")
        if filename_graph != "" and os.path.exists(filename_graph):
            Logger.log("The knowledge graph file > " + filename_graph + " exists.")
            break
        else:
            Logger.log("Unable to read the specified filename > " + filename_graph, Logger.LogLevel.ERROR)

    return load_input_files(filename_queries, filename_corpus, filename_graph)
