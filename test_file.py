import sys
import os

from fileio import *

# Unit Tests
class TestFileIOFunctions(unittest.TestCase):
    def setUp(self):
        self.filename = 'test.txt'
        self.test_string = 'Hello, World!'
        write_string_to_file(self.test_string, self.filename)

    def tearDown(self):
        try:
            os.remove(self.filename)
            os.remove('copy_' + self.filename)
        except FileNotFoundError:
            pass

    def test_write_read_string(self):
        self.assertEqual(read_string_from_file(self.filename), self.test_string)

    def test_append_string(self):
        append_string_to_file(self.test_string, self.filename)
        self.assertEqual(read_string_from_file(self.filename), self.test_string + self.test_string)

    def test_copy_file_content(self):
        copy_file_content(self.filename, 'copy_' + self.filename)
        self.assertEqual(read_string_from_file('copy_' + self.filename), self.test_string)

    def test_count_lines(self):
        create_file_with_numbers(self.filename, 5)
        self.assertEqual(count_lines(self.filename), 5)

    def test_find_string(self):
        self.assertEqual(find_string_in_file('World', self.filename), 1)

    def test_delete_line(self):
        create_file_with_numbers(self.filename, 3)
        delete_line(self.filename, 2)
        self.assertEqual(read_string_from_file(self.filename), '1\n3\n')

    def test_replace_line(self):
        create_file_with_numbers(self.filename, 3)
        replace_line(self.filename, 2, 'replaced')
        self.assertEqual(read_string_from_file(self.filename), '1\nreplaced\n3\n')


    def test_create_file_with_numbers(self):
        create_file_with_numbers(self.filename, 3)
        self.assertEqual(read_string_from_file(self.filename), '1\n2\n3\n')
    
    def test_most_frequent_word(self):
        # Set up a sample string where "hello" and "world" both appear three times, but "hello" appears first.
        sample_string = "Hello world. Hello again. Goodbye Hello world. Testing world."
        write_string_to_file(sample_string, self.filename)
        result = most_frequent_word(self.filename)
        self.assertEqual(result, "hello")  # 'hello' should

    def test_average_word_length(self):
        # Using a sample string "Hello world. Testing average." which has word lengths: 5, 5, 7, 7; Total words: 4; Average: 24/4 = 6
        sample_string = "Hello world. Testing average."
        write_string_to_file(sample_string, self.filename)
        result = average_word_length(self.filename)
        self.assertAlmostEqual(result, 6.5, 2)

if __name__ == '__main__':
    unittest.main()
