
class Repository:

    def __init__(self, connector):
        self.connector = connector
        pass

    def create_tables(self): pass
    def insert(self, value): pass
    def select_all(self): pass
    def select_one(self, unique_id): pass
    def delete_one(self, unique_id): pass
