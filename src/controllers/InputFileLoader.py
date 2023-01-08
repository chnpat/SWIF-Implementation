from src.controllers.CorpusLoader import CorpusLoader
from src.controllers.GraphLoader import GraphLoader
from src.controllers.QueryLoader import QueryLoader
from src.controllers.utilities import Logger


def load_input_files(filename_queries, filename_corpus, filename_graph):
    queries_loader = QueryLoader(filename_queries)
    Logger.log("The queries file : " + filename_queries + " is loaded successfully with " +
               str(len(queries_loader.queries)) + " requirements.", Logger.LogLevel.INFO)
    print("The queries file : " + filename_queries + " is loaded successfully with " +
          str(len(queries_loader.queries)) + " requirements.")

    corpus_loader = CorpusLoader(filename_corpus)
    Logger.log("The corpus file : " + filename_corpus + " is loaded successfully with " +
               str(len(corpus_loader.entries)) + " entries.", Logger.LogLevel.INFO)
    print("The corpus file : " + filename_corpus + " is loaded successfully with " +
          str(len(corpus_loader.entries)) + " entries.")

    graph_loader = GraphLoader(filename_graph)
    Logger.log("The knowledge graph file : " + filename_graph + " is loaded successfully with " +
               str(len(graph_loader.facts)) + " facts.", Logger.LogLevel.INFO)
    print("The knowledge graph file : " + filename_graph + " is loaded successfully with " +
          str(len(graph_loader.facts)) + " facts.")

    return queries_loader, corpus_loader, graph_loader
