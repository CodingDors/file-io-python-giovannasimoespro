import unittest
import os


# Problem 1: Write a function to write a string to a file -> COMPLETED FOR YOU
def write_string_to_file(s, filename):
    """
    Writes a string to a specified file.

    Args:
    - s (str): The string to be written to the file.
    - filename (str): The name of the file.

    Returns:
    None
    """
    with open(filename, 'w') as f:
        f.write(s)
        
# Problem 2: Write a function to read a string from a file.
def read_string_from_file(filename):
    """
    Reads the entire content of a file as a string.

    Args:
    - filename (str): The name of the file.

    Returns:
    str: The content of the file.
    """

# Problem 3: Write a function to append a string to a file.
def append_string_to_file(s, filename):
    """
    Appends a string to the end of a specified file.

    Args:
    - s (str): The string to be appended.
    - filename (str): The name of the file.

    Returns:
    None
    """


# Problem 4: Write a function to copy contents from one file to another.
def copy_file_content(src, dest):
    """
    Copies the content of one file to another.

    Args:
    - src (str): The source file.
    - dest (str): The destination file.

    Returns:
    None
    """


# Problem 5: Write a function to create a file with N lines of numbers from 1 to N.
def create_file_with_numbers(filename, N):
    """
    Creates a file with N lines of numbers, from 1 to N.

    Args:
    - filename (str): The name of the file to be created.
    - N (int): The number of lines/numbers.

    Returns:
    None
    """


# Problem 6: Write a function to count the number of lines in a file.
def count_lines(filename):
    """
    Counts the number of lines in a file.

    Args:
    - filename (str): The name of the file.

    Returns:
    int: The number of lines in the file.
    """
    

# Problem 7: Write a function to find a string in a file and return the line number.
def find_string_in_file(s, filename):
    """
    Searches for a string in a file and returns the line number where it was found.

    Args:
    - s (str): The string to be searched.
    - filename (str): The name of the file.

    Returns:
    int: The line number where the string was found or None if not found.
    """


# Problem 8: Write a function to delete a specific line from a file.
def delete_line(filename, line_number):
    """
    Deletes a specific line from a file.

    Args:
    - filename (str): The name of the file.
    - line_number (int): The line number to be deleted.

    Returns:
    None
    """

# Problem 9: Write a function to replace a specific line in a file.
def replace_line(filename, line_number, new_line):
    """
    Replaces a specific line in a file with a new line.

    Args:
    - filename (str): The name of the file.
    - line_number (int): The line number to be replaced.
    - new_line (str): The new line content.

    Returns:
    None
    """

#Problem 10 Calculate the most frequent word in a dictionary
def most_frequent_word(filename):
    """
    Determines and returns the most frequent word in a file.
    
    If multiple words have the same highest frequency, the function should return the word 
    that appears first in the file. Words are considered case-insensitive and are delimited by whitespace.

    Parameter:
    - filename (str): The path of the file from which to determine the most frequent word.
    
    Returns:
    - str: The most frequent word in the file.
    """
    

#Problem 11
def average_word_length(filename):
    """
    Determines and returns the average length of words in a file.
    
    Words are considered case-insensitive and are delimited by whitespace.

    Parameter:
    - filename (str): The path of the file from which to determine the average word length.
    
    Returns:
    - float: The average length of words in the file.
    """



def run_example_operations():
    print("Running example operations...\n")
    
    filename = "example.txt"
    filename_copy = "example_copy.txt"
    append_text = " Appended Text!"
    line_number = 3
    replacement_text = "This line has been replaced."
    
    # Example 1: write_string_to_file
    write_string_to_file("Hello, World!", filename)
    print(f"1. Written to {filename}: Hello, World!")
    
    # Example 2: read_string_from_file
    # read_content = read_string_from_file(filename)
    # print(f"2. Read from {filename}: {read_content}")
    
    # # Example 3: append_string_to_file
    # append_string_to_file(append_text, filename)
    # print(f"3. Appended to {filename}: {append_text}")
    # print(f"   New content: {read_string_from_file(filename)}")
    
    # # Example 4: copy_file_content
    # copy_file_content(filename, filename_copy)
    # print(f"4. Copied content from {filename} to {filename_copy}.")
    # print(f"   Content in {filename_copy}: {read_string_from_file(filename_copy)}")

    # Example 5: create_file_with_numbers
    # create_file_with_numbers("numbers.txt", 5)
    # print(f"10. Created a new file with numbers from 1 to 5.")
    # print(f"    Content: {read_string_from_file('numbers.txt')}")
    
    # # Example 6: count_lines
    # num_lines = count_lines(filename)
    # print(f"5. Number of lines in {filename}: {num_lines}")
    
    # # Example 7: find_string_in_file
    # string_to_find = "World"
    # line_found = find_string_in_file(string_to_find, filename)
    # print(f"6. String '{string_to_find}' found in {filename} at line: {line_found}")
    
    # # Example 8: delete_line
    # delete_line(filename, line_number)
    # print(f"7. Deleted line {line_number} from {filename}.")
    # print(f"   New content: {read_string_from_file(filename)}")
    
    # # Example 9: replace_line
    # replace_line(filename, line_number, replacement_text)
    # print(f"8. Replaced line {line_number} in {filename} with: {replacement_text}")
    # print(f"   New content: {read_string_from_file(filename)}")

    # Example 10: most_frequent_word
    # frequent_word = most_frequent_word(filename)
    # print(f"12. Most frequent word in {filename}: {frequent_word}")

    # Example 11: average_word_length
    # avg_word_len = average_word_length(filename)
    # print(f"11. Average word length in {filename}: {avg_word_len}")

    
if __name__ == "__main__":
    run_example_operations()