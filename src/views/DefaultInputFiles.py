import os.path

from src import global_var
from src.controllers.InputFileLoader import load_input_files
from src.controllers.utilities import Logger


def default_filename_load():

    filename_queries = global_var.DIR_REQUIREMENTS
    if os.path.exists(filename_queries):
        Logger.log("The queries file > " + filename_queries + " exists.", Logger.LogLevel.INFO)
    else:
        Logger.log("Unable to read the queries input file > " + global_var.DIR_REQUIREMENTS, Logger.LogLevel.ERROR)

    filename_corpus = global_var.DIR_WEAKNESSES
    if os.path.exists(filename_corpus):
        Logger.log("The corpus file : " + filename_corpus + " exists.")
    else:
        Logger.log("Unable to read the weaknesses input file > " + global_var.DIR_WEAKNESSES, Logger.LogLevel.ERROR)

    filename_graph = global_var.DIR_KG
    if os.path.exists(filename_graph):
        Logger.log("The knowledge graph file : " + filename_graph + " exists.")
    else:
        Logger.log("Unable to read the knowledge graph input file > " + global_var.DIR_KG, Logger.LogLevel.ERROR)

    return load_input_files(filename_queries, filename_corpus, filename_graph)
