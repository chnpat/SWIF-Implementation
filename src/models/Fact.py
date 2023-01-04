import enum


class Relation(enum.Enum):
    NONE = 0
    CORRELATE_WITH = 1
    SYNONYM_OF = 2


class Fact:

    def __init__(self, generic="", relation=Relation.NONE, specific=""):
        self.generic = generic
        self.relation = relation
        self.specific = specific

    def get_generic(self):
        return self.generic

    def get_relation(self):
        return self.relation

    def get_specific(self):
        return self.specific

    def set_generic(self, generic=""):
        self.generic = generic

    def set_relation(self, relation=Relation.NONE):
        self.relation = relation

    def set_specific(self, specific=""):
        self.specific = specific
