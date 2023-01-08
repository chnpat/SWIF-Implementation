from xml.dom import minidom

from src import global_var
from src.models.Fact import Fact, Relation
from src.controllers.utilities import Logger


class GraphLoader:

    def __init__(self, directory=global_var.DIR_KG):
        self.facts = []
        self.load_graph_xml(directory)

    def load_graph_xml(self, directory):
        try:
            with minidom.parse(directory) as dom:
                facts = dom.getElementsByTagName("fact")
                for fact in facts:
                    relation = Relation.NONE
                    if fact.attributes["relation"].value == "correlate_with":
                        relation = Relation.CORRELATE_WITH
                    elif fact.attributes["relation"].value == "synonym_of":
                        relation = Relation.SYNONYM_OF
                    self.facts.append(Fact(fact.attributes["generic"].value, relation, fact.firstChild.data))
        except IOError:
            Logger.log("Unable to read the knowledge graph input file > " + directory, Logger.LogLevel.ERROR)

    def search(self, word):
        result = []
        for fact in self.facts:
            if fact.generic == word:
                result.append(fact.specific)
            elif fact.specific == word:
                result.append(fact.generic)
        return result
