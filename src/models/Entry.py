class Entry:

    def __init__(self, cwe_id="", name="", description="", extend="", clean="", vector=[]):
        self.cweId = cwe_id
        self.name = name
        self.description = description
        self.extend = extend
        self.clean = clean
        self.vector = vector

    def get_id(self):
        return self.cweId

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_extend(self):
        return self.extend

    def get_clean(self):
        return self.clean

    def get_vector(self):
        return self.vector

    def set_id(self, cwe_id=""):
        self.cweId = cwe_id

    def set_name(self, name=""):
        self.name = name

    def set_description(self, description=""):
        self.description = description

    def set_extend(self, extend=""):
        self.extend = extend

    def set_clean(self, clean=""):
        self.clean = clean

    def set_vector(self, vector=[]):
        self.vector = vector
