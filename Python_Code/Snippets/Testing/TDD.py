"""
    Test Driven Development
    Write the tests ( THIS file, with test functions()) before you create your program (normal_functions() ).
    make sure you know your requirements or wishes!

# program will:
# 1, Take in a filename argument
# 2, Read a file
# 3, Calculate number of lines and characters

"""

import unittest  # (unitest module is NOT PEP8! So norm_func_looks_like_this()  testFuncLooksLikeThis()
import os

#filename = 'text_analysis_test_file.txt'


def analyze_text(filename):
    """Calculate the number of lines and characters in a file.
    :param
        filename: The name of the file to analyze
    Raises:
        IOError: If ''filename'' does not exist or can't be read
    :v1 returns: The number of lines in the file
                    with open(filename, 'r') as f:
                        return sum(1 for _ in f)

    v2 returns: A tuple where
                the first element is the "number of lines" in the file and
                the second element is the "number of characters".
    """
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
        return lines, chars


class TextAnalysisTests(unittest.TestCase):
    """Test for the ''analyze_text()'' function. """

    def setUp(self):  # Test method (called fixure) for setting up the test environment vars  (comes from unittest.setUp)
        """Fixture that creates a file for the text methods to use"""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great civil war.\n'
                    'testing whether that nation,\n'
                    'or any nation so conceived and so dedicated,\n'
            #        'can long endure.\n'
                    'can long endure.'
                    )


    def tearDown(self): # Test method (called fixure) for tearing down text environment
        """Fixture that deletes the files used by the test methods"""
        try:
            os.remove(self.filename)
        except:
            pass


    def test_function_runs(self):
        """Basic smoke test: does the function run."""
        analyze_text(self.filename)

    # Test case
    def test_line_count(self):
        """Check that the line count is correct."""
        #self.assertEqual(Expected, Actual, Message )
        self.assertEqual(4, analyze_text(self.filename)[0], "Line count:")


    # Test case
    def test_character_count(self):
        """Check that the char count is correct"""
        self.assertEqual(131, analyze_text(self.filename)[1], "Character count:")


    def test_no_such_filename(self):
        """meh"""
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        """Check that the function doesn't delete the input file."""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))



if __name__ == '__main__':
    unittest.main()
