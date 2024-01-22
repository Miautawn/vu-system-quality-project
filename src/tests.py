import unittest
from unittest.mock import MagicMock, patch
from main import get_occupied_rooms, get_all_guests 

class TestGetOccupiedRooms(unittest.TestCase):

    def test_get_occupied_rooms(self):
        # Create a mock cursor that can iterate over a list of dictionaries
        mock_cursor = MagicMock()
        mock_cursor.__iter__.return_value = iter([
            {"keys": [{"room_number": 101}]},
            {"keys": [{"room_number": 102}]},
            {"keys": [{"room_number": 103}]}
        ])
        
        # Create a mock client with a `find` method that returns the mock cursor
        mock_client = MagicMock()
        mock_client.find.return_value = mock_cursor

        occupied_rooms = get_occupied_rooms(mock_client)
        self.assertEqual(occupied_rooms, [101, 102, 103])

        # Test a case, where there are no occupied rooms
        mock_cursor = MagicMock()
        mock_cursor.__iter__.return_value = iter([
        ])
        
        # Create a mock client with a `find` method that returns the mock cursor
        mock_client = MagicMock()
        mock_client.find.return_value = mock_cursor

        occupied_rooms = get_occupied_rooms(mock_client)
        self.assertEqual(occupied_rooms, [])

    def test_get_all_guests(self):
        # Create a mock cursor that can iterate over a list of dictionaries
        mock_cursor = MagicMock()
        mock_cursor.__iter__.return_value = iter([
            {"name": "name1", "surname": "surname1"},
            {"name": "name2", "surname": "surname2"},
        ])
        
        # Create a mock client with a `find` method that returns the mock cursor
        mock_client = MagicMock()
        mock_client.find.return_value = mock_cursor

        occupied_rooms = get_all_guests(mock_client)
        self.assertEqual(occupied_rooms, [["name1", "surname1"], ["name2", "surname2"]])

        # test a case, where there are no guests
        mock_cursor = MagicMock()
        mock_cursor.__iter__.return_value = iter([
        ])
        
        # Create a mock client with a `find` method that returns the mock cursor
        mock_client = MagicMock()
        mock_client.find.return_value = mock_cursor

        occupied_rooms = get_all_guests(mock_client)
        self.assertEqual(occupied_rooms, [])

if __name__ == '__main__':
    unittest.main()
