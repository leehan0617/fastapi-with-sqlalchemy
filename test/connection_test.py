import unittest
from database.connection import Connection


class ConnectionTest(unittest.TestCase):
    def test_connection(self):
        conn = Connection()
        connection = conn.get_connection()
        print(connection)

    def test_get_table_info(self):
        conn = Connection()
        table = conn.get_table_info('login_user')
        print(table.columns.keys())
