from repository import Repository


class UserRepository(Repository):

    def __init__(self, connector):
        super().__init__(connector)

    def create_tables(self):
        self.connector.execute(
            "CREATE TABLE Users( "
            "id TEXT NOT NULL UNIQUE PRIMARY KEY, "
            "experience INTEGER NOT NULL DEFAULT 0 "
            ");"
        )
        self.connector.commit()

    def insert(self, value):
        self.connector.execute(
            "INSERT OR REPLACE INTO Users(id, experience) VALUES (?,?);"
        )
        self.connector.commit()

    def select_all(self):
        stmt = self.connector.execute(
            "SELECT * FROM Users;"
        )

        rows = stmt.fetchAll()

        return rows

    def select_one(self, unique_id):
        stmt = self.connector.execute("SELECT * FROM Users WHERE id=?;", unique_id)
        rows = stmt.fetchAll()

        if len(rows) > 0:
            return rows[0]
        else:
            return None
        pass

    def delete_one(self, unique_id):
        stmt = self.connector.execute("DELETE FROM Users WHERE id=?", unique_id)
        self.connector.commit()
