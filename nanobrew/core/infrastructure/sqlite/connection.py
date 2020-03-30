import aiosqlite

class Connection:
    _database_name: str
    _connection: aiosqlite.Connection

    def __init__(self, database_name):
        self._database_name = database_name
        self._connection = None

    async def get_connection(self) -> aiosqlite.Connection: 
        if self._connection is None:
            connection = await aiosqlite.connect(self._database_name)
            connection.row_factory = aiosqlite.Row

            self._connection = connection

        return self._connection

