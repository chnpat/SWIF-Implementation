from xml.dom import minidom

from src import global_var
from src.models.Requirement import Requirement
from src.controllers.utilities import Logger


class QueryLoader:

    def __init__(self, directory=global_var.DIR_REQUIREMENTS):
        self.queries = []
        self.load_requirements_xml(directory)

    def load_requirements_xml(self, directory):
        try:
            with minidom.parse(directory) as dom:
                queries = dom.getElementsByTagName("function")
                for requirement in queries:
                    r = Requirement(requirement.firstChild.data)
                    self.queries.append(r)
        except IOError:
            Logger.log("Unable to read the queries input file > " + directory, Logger.LogLevel.ERROR)
