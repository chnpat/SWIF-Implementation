from src import global_var


class SWIF:

    def __init__(self):
        self.s = 0
        print("====================================")
        print("SSI Weakness Identification Framework V." + global_var.VERSION)
        print("====================================")
        self.default_files_flag = input("Do you want to specify input files manually? [Y/N] : ")
        print(self.default_files_flag)


if __name__ == "__main__":
    recommender = SWIF()
