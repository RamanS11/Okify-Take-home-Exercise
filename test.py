import unittest
from main import get_project_status


class TestFunction(unittest.TestCase):

    def test_get_project_status(self):
        """
        Function created to test the get_project_status function with the given examples
        :return:
        """
        # Test case 1
        mock_input_status_1 = ["Requested", "Requested", "Requested"]
        self.assertEqual("Requested", get_project_status(mock_input_status_1))

        # Test case 2
        mock_input_status_2 = ["Activated", "Activated", "Canceled"]
        self.assertEqual("Activated", get_project_status(mock_input_status_2))

        # Test case 3
        mock_input_status_3 = ["Requested", "Processed", "Canceled"]
        self.assertEqual("Processed", get_project_status(mock_input_status_3))

        # Test case 4
        mock_input_status_4 = ["Processed", "Missing info", "Processed"]
        self.assertEqual("Missing info", get_project_status(mock_input_status_4))


if __name__ == "__main__":
    unittest.main()
