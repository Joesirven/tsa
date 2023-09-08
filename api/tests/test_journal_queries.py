import unittest
from unittest.mock import patch, Mock
from queries.journals import JournalRepository, JournalOut

class TestJournalRepository(unittest.TestCase):

    def setUp(self):
        self.repo = JournalRepository()
        self.mock_entry = (1, "location", "picture_url", "description", 5, "2023-01-01", 1)

    @patch('queries.journals.pool')
    def test_get_one_success(self, mock_pool):
        # Mocking the database connection and cursor fetch
        mock_conn = mock_pool.connection().__enter__()
        mock_cursor = mock_conn.cursor().__enter__()
        mock_cursor.fetchone.return_value = self.mock_entry

        journal = self.repo.get_one(1)

        # Assertions
        if not isinstance(journal, JournalOut):
            self.fail(f"Expected JournalOut but got error: {journal}")

        self.assertEqual(journal.id, 1)
        self.assertEqual(journal.location, "location")

    @patch('queries.journals.pool')
    def test_get_one_not_found(self, mock_pool):
        # Mocking the database connection and cursor fetch to return None
        mock_conn = mock_pool.connection().__enter__()
        mock_cursor = mock_conn.cursor().__enter__()
        mock_cursor.fetchone.return_value = None

        journal = self.repo.get_one(1)

        # Assertions
        expected_error = {"message": "could not get journal entry"}
        self.assertEqual(journal, expected_error, f"Expected error message but got: {journal}")

if __name__ == '__main__':
    unittest.main()
