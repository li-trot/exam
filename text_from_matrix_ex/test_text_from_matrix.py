import unittest
from text_from_matrix import text_from_matrix


class TestTextFromMatrix(unittest.TestCase):
    def test_text_from_matrix(self):
        """Check output."""
        # Test case 1
        matrix = [
            ['A', 'B', 'C', 'D'],
            ['E', 'F', 'G', 'H'],
            ['I', 'J', 'K', 'L'],
            ['M', 'N', 'O', 'P'],
        ]
        expected_output = 'ACFHIKNP'
        self.assertEqual(text_from_matrix(matrix), expected_output)

        # Test case 2
        matrix = [
            ['A', 'B', 'C'],
            ['D', 'E', 'F'],
            ['G', 'H', 'I'],
        ]
        expected_output = 'ACEGI'
        self.assertEqual(text_from_matrix(matrix), expected_output)

        # Test case 3
        matrix = [
            ['A', 'B'],
            ['C', 'D'],
        ]
        expected_output = 'AD'
        self.assertEqual(text_from_matrix(matrix), expected_output)

    def test_text_from_matrix_invalid_input(self):
        # Test case 4
        matrix_with_unequal_columns = [
            ['A', 'B', 'C'],
            ['D', 'E'],
        ]
        self.assertRaises(AttributeError, text_from_matrix,
                          matrix_with_unequal_columns)

        # Test case 5
        matrix_with_non_letters = [
            ['A', 'B', 'C'],
            ['D', 'E', 1],
        ]
        self.assertRaises(AttributeError, text_from_matrix,
                          matrix_with_non_letters)


if __name__ == '__main__':
    unittest.main()
