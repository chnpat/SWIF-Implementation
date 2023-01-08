from utilities import FileHandler
from src import global_var
from src.models.Entry import Entry


class CorpusPreparer:

    def __init__(self, read_csv=True):
        self.entries = []
        if read_csv:
            print("read from the CSV file.")
            self.load_corpus_csv()
        else:
            print("crawl from the website.")

    def load_corpus_csv(self):
        entries = FileHandler.read_csv(global_var.DIR_WEAKNESSES_CSV)
        for entry in entries:
            e = Entry(entry["id"], entry["name"], entry["description"], entry["extendedDescription"], "", [])
            self.entries.append(e)

