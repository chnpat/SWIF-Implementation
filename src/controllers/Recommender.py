import pandas as pd
from src.controllers.CorpusLoader import CorpusLoader
from src.controllers.Vectorizer import Vectorizer
from sklearn.metrics.pairwise import cosine_similarity


def retrieve_and_rank(query, corpus_loader, graph_loader, preprocessor, vectorizer):
    corpus_list = []
    if isinstance(corpus_loader, CorpusLoader) and isinstance(vectorizer, Vectorizer):
        for entry in corpus_loader.entries:
            corpus_dict = {"id": entry.get_id(), "name": entry.get_name(), "description": entry.get_description(),
                           "extended_description": entry.get_extend(), "clean": entry.get_clean(),
                           "vector": entry.get_vector()}
            corpus_list.append(corpus_dict)

        corpus_df = pd.DataFrame(corpus_list)
        query_vect = vectorizer.vectorize(query, preprocessor, graph_loader)
        query_list = query_vect.toarray().tolist()
        query_input = []
        for index in range(len(corpus_df["vector"].tolist())):
            query_input.append(query_list[0])

        score = cosine_similarity(corpus_df["vector"].tolist(), query_list)
        score = [score[index][0] for index in range(len(score))]
        return score


def vote_by_weight(score_list, max_result, min_weight):
    ranked_list = []
    index_list = []
    result_list = []
    for j in range(len(score_list)):
        ranked = sorted([(index, value) for index, value in enumerate(score_list[j])], key=lambda x: x[1])[-max_result:]
        for pair in ranked:
            if pair[0] not in index_list:
                index_list.append(pair[0])
        ranked_list.append(ranked)

    for index in index_list:
        count = 0
        for lst in ranked_list:
            for item in lst:
                if item[0] == index:
                    count = count + 1
        weight = count / len(ranked_list)
        if weight >= min_weight:
            result_list.append(index)
    return result_list, index_list
