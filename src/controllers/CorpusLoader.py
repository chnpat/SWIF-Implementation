from xml.dom import minidom
from src import global_var
from src.controllers.GraphLoader import GraphLoader
from src.controllers.Preprocessor import Preprocessor
from src.controllers.utilities import Logger
from src.models.Entry import Entry


def check_none(node):
    if node is not None and node.firstChild is not None:
        return node.firstChild.data
    else:
        return ""


def transform_vector(vect_string):
    vect_string = vect_string.strip("[]")
    vect_list = []
    if vect_string != "":
        vect_values_list = vect_string.split(", ")
        vect_list = [float(val) for val in vect_values_list]
    return vect_list


class CorpusLoader:

    def __init__(self, directory=global_var.DIR_WEAKNESSES):
        self.entries = []
        self.load_corpus_xml(directory)

    def load_corpus_xml(self, directory):
        try:
            with minidom.parse(directory) as dom:
                if len(self.entries) > 0:
                    self.entries = []

                entries = dom.getElementsByTagName("entry")
                for entry in entries:
                    cweId = entry.attributes["id"].value
                    name = entry.attributes["name"].value
                    description = check_none(entry.getElementsByTagName("description")[0])
                    extend = check_none(entry.getElementsByTagName("extendedDescription")[0])
                    clean = check_none(entry.getElementsByTagName("cleanText")[0])
                    vector = transform_vector(check_none(entry.getElementsByTagName("vector")[0]))

                    self.entries.append(Entry(cweId, name, description, extend, clean, vector))
        except IOError:
            Logger.log("Error reading the DOM XML file > " + global_var.DIR_WEAKNESSES, Logger.LogLevel.ERROR)

    def vectorize_entry(self, vector_model, preprocessor, graph_loader):
        new_entries = []
        if isinstance(preprocessor, Preprocessor) and isinstance(graph_loader, GraphLoader):
            for entry in self.entries:
                if entry.get_clean() != "":
                    vector = vector_model.vectorize(entry.get_clean(), preprocessor, graph_loader)
                    if entry.vector != vector.toarray().tolist()[0]:
                        entry.set_vector(vector.toarray().tolist()[0])
                    new_entries.append(entry)
        print("Entries in the corpus are vectorized successfully.")
        self.entries = new_entries
