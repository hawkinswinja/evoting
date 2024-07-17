import unittest
from engine import Engine  # Import the Engine class from your module
from models import Voter  # Import the Voter model class

class TestEngine(unittest.TestCase):

    def setUp(self):
        """Set up the test environment"""
        self.engine = Engine()
        self.engine.reload()  # Initialize the session

    def tearDown(self):
        """Tear down after each test"""
        self.engine.destroy()  # Clean up the database after each test

    def test_create_voter(self):
        """Test creation of a Voter object"""
        voter_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'auth_id': 'secure_password'
            # Add other required fields as needed
        }

        # Create a new voter using the Engine
        self.engine.new('Voter', voter_data)
        self.engine.save()  # Commit changes to the database

        # Retrieve the created voter from the database
        created_voter = self.engine.show('Voter', 1)  # Assuming voter_id 1 is created

        # Assertions to verify the created voter
        self.assertIsNotNone(created_voter)
        self.assertEqual(created_voter.name, voter_data['name'])
        self.assertEqual(created_voter.email, voter_data['email'])
        self.assertEqual(created_voter.is_admin, False)
        # Add more assertions based on your Voter model attributes

if __name__ == '__main__':
    unittest.main()

