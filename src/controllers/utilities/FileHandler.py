import csv
import pickle
import Logger


def read_csv(directory):
    try:
        data = []
        with open(directory, "r") as file:
            reader = csv.DictReader(file)
            for line in reader:
                data.append(line)
            if len(data) > 0:
                return data
            else:
                return []
    except IOError:
        Logger.log("Error reading a CSV file > " + directory, Logger.LogLevel.ERROR)
    finally:
        file.close()


def write_csv(directory, data_dict, fields):
    try:
        with open(directory, "w") as file:
            if len(fields) > 0:
                writer = csv.DictWriter(directory, fieldnames=fields)
                writer.writeheader()
            else:
                writer = csv.DictWriter(directory, fieldnames=[])

            if len(data_dict) > 0:
                for row_dict in data_dict:
                    writer.writerow(row_dict)
    except IOError:
        Logger.log("Error writing a CSV file > " + directory, Logger.LogLevel.ERROR)
    finally:
        file.close()


def read_pickle(directory):
    try:
        with open(directory, "rb") as file:
            data = pickle.load(file)
            return data
    except IOError:
        Logger.log("Error reading a Pickle file > " + directory, Logger.LogLevel.ERROR)
    finally:
        file.close()


def write_pickle(directory, data):
    try:
        with open(directory, "wb") as file:
            pickle.dump(data, file)
    except IOError:
        Logger.log("Error writing a Pickle file > " + directory, Logger.LogLevel.ERROR)
    finally:
        file.close()


def read_text(directory):
    try:
        with open(directory, "r") as file:
            data_lines = []
            for line in file:
                data_lines.append(line)
            if len(data_lines) > 0:
                return data_lines
    except IOError:
        Logger.log("Error reading a text file > " + directory, Logger.LogLevel.ERROR)
    finally:
        file.close()
        return None


def write_text(directory, data):
    try:
        with open(directory, "w") as file:
            file.write(data)
    except IOError:
        Logger.log("Error writing a text file > " + directory, Logger.LogLevel.ERROR)
    finally:
        file.close()
