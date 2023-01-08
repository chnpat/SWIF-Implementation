import os.path

from src import global_var
from src.controllers.utilities import FileHandler
from src.controllers.Preprocessor import Preprocessor
from src.controllers.CorpusLoader import CorpusLoader
from src.controllers.GraphLoader import GraphLoader
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


class Vectorizer:

    def __init__(self):
        vect_model_dir = global_var.DIR_VECTOR_MODEL
        if os.path.exists(vect_model_dir):
            self.vect_model = FileHandler.read_pickle(vect_model_dir)

    def vectorize(self, text, preprocessor, graph_loader):
        if isinstance(preprocessor, Preprocessor):
            clean_text = preprocessor.preprocess(text, graph_loader)
            return self.vect_model.transform([clean_text])

    def train_vect_model(self, preprocessor, graph_loader, corpus_loader):
        if isinstance(corpus_loader, CorpusLoader) and isinstance(graph_loader, GraphLoader):
            self.vect_model = TfidfVectorizer()
            text = []
            for entry in corpus_loader.entries:
                pair = (entry.cweId, entry.name + " " + entry.description + " " + entry.extend)
                entry.clean = preprocessor.preprocess(pair[1], graph_loader)
                text.append(entry.clean)
            tfidf_count_occurs = self.vect_model.fit_transform(text)
            vect = tfidf_count_occurs.toarray().tolist()
            FileHandler.write_pickle(global_var.DIR_VECTOR_MODEL, self.vect_model)
            return self.vect_model, vect
