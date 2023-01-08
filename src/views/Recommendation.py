from src import global_var
from src.controllers.CorpusLoader import CorpusLoader
from src.controllers.QueryLoader import QueryLoader
from src.controllers.Recommender import retrieve_and_rank, vote_by_weight
from src.controllers.utilities import FileHandler
from src.models.Requirement import Requirement


def recommend(queries_loader, corpus_loader, graph_loader, preprocessor, vectorizer):
    if isinstance(queries_loader, QueryLoader):
        sim_scores = []
        for r in queries_loader.queries:
            if isinstance(r, Requirement):
                sim_scores.append(retrieve_and_rank(r.requirement, corpus_loader, graph_loader, preprocessor,
                                                    vectorizer))
        return vote_by_weight(sim_scores, global_var.MAX_RECOMMENDED_RESULTS, global_var.MIN_WEIGHT)


def evaluate(result, index_list, corpus_loader):
    TP, TN, FP, FN = 0, 0, 0, 0
    recommend_id = []
    truth = FileHandler.read_csv(global_var.DIR_WEAKNESSES_CSV)
    if isinstance(corpus_loader, CorpusLoader):
        for index, entry in enumerate(corpus_loader.entries):
            if index in result:
                recommend_id.append(entry.get_id())
        for line in truth:
            if line["id"] in recommend_id:
                if line["actual"] == "1":
                    TP += 1
                else:
                    FP += 1
            else:
                if index_list is not None and line["id"] in index_list:
                    if line["actual"] == "1":
                        FN += 1
                    else:
                        TN += 1
                else:
                    if line["actual"] == "1":
                        FN += 1
                    else:
                        TN += 1

        if (TP + FP + FN + TN) != 0 or (TP + FP) != 0 or (TP + FN) != 0:
            precision = TP / (TP + FP)
            recall = TP / (TP + FN)
            print("Precision = " + str(precision))
            print("Recall = " + str(recall))
            print("F1-Score = " + str(2 * ((precision * recall) / (precision + recall))))
            print("Accuracy = " + str((TP + TN) / (TP + FP + FN + TN)))
        else:
            print("Accuracy = 0")
