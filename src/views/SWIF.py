from src import global_var
from src.controllers.Preprocessor import Preprocessor
from src.controllers.Vectorizer import Vectorizer
from src.views.DefaultInputFiles import default_filename_load
from src.views.ManualInputFiles import filename_inquiries
from src.views.Recommendation import recommend, evaluate


class SWIF:

    def __init__(self):
        self.preprocessor = Preprocessor()
        self.vectorizer = Vectorizer()

        print("====================================")
        print("SSI Weakness Identification Framework V." + global_var.VERSION)
        print("====================================")

        while True:
            self.default_files_flag = input("Would you like to specify input files manually? [Y/N] : ")
            print("--------------------------")
            if self.default_files_flag == "Y":
                queries_loader, corpus_loader, graph_loader = filename_inquiries()
                break
            elif self.default_files_flag == "N":
                queries_loader, corpus_loader, graph_loader = default_filename_load()
                break
            else:
                print("Invalid input command.")

        if queries_loader is not None and corpus_loader is not None and graph_loader is not None:
            print("--------------------------")
            self.train_vectorizer_flag = input("Would you like to re-train the term vectorizer? [Y/N] : ")
            if self.train_vectorizer_flag == "Y":
                self.vectorizer.train_vect_model(self.preprocessor, graph_loader, corpus_loader)
                self.vectorizer = Vectorizer()

            print("--------------------------")
            result, index_list = recommend(queries_loader, corpus_loader, graph_loader, self.preprocessor,
                                           self.vectorizer)
            print("Recommended SSI-Specific Weaknesses:")
            for r in result:

                print("CWE-" + str(r) + ", ", end="")
            print()
            print("--------------------------")

            while True:
                self.evaluate_flag = input("Would you like to evaluate the performance against the ground truth? ["
                                           "Y/N] : ")
                if self.evaluate_flag == "Y":
                    print("--------------------------")
                    evaluate(result, index_list, corpus_loader)
                    break
                elif self.evaluate_flag == "N":
                    break
                else:
                    print("Invalid input command.")
            print("--------------------------")
            print("Thank you for using the SWIF implementation.")


if __name__ == "__main__":
    recommender = SWIF()
