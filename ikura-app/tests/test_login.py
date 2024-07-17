import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, session, flash, redirect, url_for, request, render_template
from  routes.routes import login 

class TestLoginFunction(unittest.TestCase):

    def setUp(self):
        """Set up the Flask application for testing"""
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.secret_key = 'your_secret_key'  # Set a secret key for session

    def test_login_valid_credentials(self):
        """Test login function with valid credentials"""
        with self.app.test_request_context('/login', method='POST',
                                          data={'user-id': '1', 'password': 'testpass'}):
            # Mock the storage and auth functions
            mock_storage = MagicMock()
            mock_user = MagicMock()
            mock_user.voter_id = 1
            mock_user.password = 'hashed_password'  # Replace with actual hashed password
            mock_user.is_admin = False  # Set accordingly based on your test case
            mock_user.status = 'Not'
            mock_storage.show.return_value = mock_user
            self.app.preprocess_request()
            with patch('routes.storage', mock_storage), \
                 patch('auth.validate', return_value=True):
                response = login()
                self.assertEqual(response.location, url_for('routes.vote', myid=1, post='first_post'))

    def test_login_invalid_user_id(self):
        """Test login function with invalid user id"""
        with self.app.test_request_context('/login', method='POST',
                                          data={'user-id': '999', 'password': 'testpass'}):
            mock_storage = MagicMock()
            mock_storage.show.return_value = None  # Simulate user not found
            self.app.preprocess_request()
            with patch('routes.storage', mock_storage):
                response = login()
                self.assertIn(b'user id does not exist', response.data)

    # Add more test cases for other scenarios: incorrect password, admin login, etc.

if __name__ == '__main__':
    unittest.main()

