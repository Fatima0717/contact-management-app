import unittest
from unittest.mock import patch
from contacts import ContactManager

class TestContactManager(unittest.TestCase):

    @patch('contacts.logging')
    def test_add_contact(self, mock_logging):
        manager = ContactManager()
        manager.add_contact("John Doe", "1234567890", "john@example.com")
        mock_logging.info.assert_called_with("Contact John Doe added successfully.")

    @patch('contacts.logging')
    def test_add_contact_existing(self, mock_logging):
        manager = ContactManager()
        manager.add_contact("John Doe", "1234567890", "john@example.com")
        manager.add_contact("John Doe", "1234567890", "john@example.com")
        mock_logging.info.assert_called_with("Contact with name John Doe already exists.")

    @patch('contacts.logging')
    def test_delete_contact(self, mock_logging):
        manager = ContactManager()
        manager.add_contact("John Doe", "1234567890", "john@example.com")
        manager.delete_contact("John Doe")
        mock_logging.info.assert_called_with("Contact John Doe deleted successfully.")

    @patch('contacts.logging')
    def test_delete_contact_not_found(self, mock_logging):
        manager = ContactManager()
        manager.delete_contact("Jane Doe")
        mock_logging.info.assert_called_with("No contact found with name Jane Doe.")

    @patch('contacts.logging')
    def test_search_contact(self, mock_logging):
        manager = ContactManager()
        manager.add_contact("John Doe", "1234567890", "john@example.com")
        manager.search_contact("John Doe")
        mock_logging.info.assert_called_with("Name: John Doe, Phone: 1234567890, Email: john@example.com")

    @patch('contacts.logging')
    def test_search_contact_not_found(self, mock_logging):
        manager = ContactManager()
        manager.search_contact("Jane Doe")
        mock_logging.info.assert_called_with("No contact found with name Jane Doe.")

    @patch('contacts.logging')
    def test_view_contacts(self, mock_logging):
        manager = ContactManager()
        manager.add_contact("John Doe", "1234567890", "john@example.com")
        manager.view_contacts()
        mock_logging.info.assert_called_with("Name: John Doe, Phone: 1234567890, Email: john@example.com")

    @patch('contacts.logging')
    def test_view_contacts_empty(self, mock_logging):
        manager = ContactManager()
        manager.view_contacts()
        mock_logging.info.assert_called_with("No contacts available.")

if __name__ == '__main__':
    unittest.main()