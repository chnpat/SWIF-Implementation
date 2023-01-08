import re
import string
import spacy

from src import global_var
from src.controllers.GraphLoader import GraphLoader

# spacy.cli.download(global_var.SPACY_PROCESSOR)
REPLACE_BY_SPACE_RE = re.compile(r'[/(){}\[\]\|@,;]')
BAD_SYMBOL_RE = re.compile(r'[^0-9a-z #+_]')
REPLACE_BY_PATTERN = [("will not", "won't"), ("shall not", "shan't"), (" not", "n\'t"), (" will", "\'ll"),
                      (" is", "\'s"), (" am", "\'m"), (" are", "\'re"), (" is", "who\'s"),
                      (", in other word,", " i.e."), (", for example,", " e.g."), ("and so on,", "etc")]


def contractions(document):
    split_doc = document.split(" ")
    result = ""
    for i in range(len(split_doc)):
        phrase = split_doc[i]
        for pair in REPLACE_BY_PATTERN:
            phrase = re.sub(pair[1], pair[0], phrase)
        result = result + " " + phrase
    return result


def clean_text(document):
    document = document.lower()
    document = contractions(document)
    document = REPLACE_BY_SPACE_RE.sub(" ", document)
    document = BAD_SYMBOL_RE.sub("", document)
    document = re.sub(r'\[.*?\]', "", document)
    document = re.sub(r'[%s]]' % re.escape(string.punctuation), "", document)
    document = re.sub(r'\w*\d\w*', "", document)
    document = re.sub(r'[‘’“”…]', "", document)
    document = re.sub(r'\n', "", document)
    return document


class Preprocessor:

    def __init__(self):
        self.preprocessor = spacy.load(global_var.SPACY_PROCESSOR)

    def preprocess(self, document, graph_loader):
        clean_document = clean_text(document)
        spacy_document = self.preprocessor(clean_document)

        lemmas = [token.lemma_ for token in spacy_document if
                  not token.is_stop and token.text != " " and token.text != ""]

        noun_chunks = []
        for token in spacy_document.noun_chunks:
            flag = True
            for word in token.text.split(" "):
                if self.preprocessor.vocab[word].is_stop:
                    flag = False
            if flag:
                noun_chunks.append(token.lemma_)

        lemmas.extend(noun_chunks)
        word_list = []
        if isinstance(graph_loader, GraphLoader):
            for lemma in lemmas:
                expand = graph_loader.search(lemma)
                if len(expand) > 0:
                    word_list.extend(expand)
            word_list.extend(lemmas)
            return " ".join([word.text for word in spacy_document if not word.is_stop and word.text != " " and
                             word.text != ""])
        else:
            return ""

