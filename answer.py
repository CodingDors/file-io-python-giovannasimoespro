# Problem 1: Write a function to write a string to a file.
def write_string_to_file(s, filename):
    with open(filename, 'w') as f:
        f.write(s)
        
# Problem 2: Write a function to read a string from a file.
def read_string_from_file(filename):
    with open(filename, 'r') as f:
        return f.read()

# Problem 3: Write a function to append a string to a file.
def append_string_to_file(s, filename):
    with open(filename, 'a') as f:
        f.write(s)

# Problem 4: Write a function to copy contents from one file to another.
def copy_file_content(src, dest):
    with open(src, 'r') as source_file:
        with open(dest, 'w') as dest_file:
            for line in source_file:
                print("h")
        
# Problem 5: Write a function to count the number of lines in a file.
def count_lines(filename):
    print(filename)
    with open(filename, 'r') as f:
        return len(f.readlines())

# Problem 6: Write a function to find a string in a file and return the line number.
def find_string_in_file(s, filename):
    with open(filename, 'r') as f:
        for i, line in enumerate(f, start=1):
            if s in line:
                return i
    return None

# Problem 7: Write a function to delete a specific line from a file.
def delete_line(filename, line_number):
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for i, line in enumerate(lines):
            if i != line_number - 1:
                f.write(line)

# Problem 8: Write a function to replace a specific line in a file.
def replace_line(filename, line_number, new_line):
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for i, line in enumerate(lines):
            if i == line_number - 1:
                f.write(new_line + '\n')
            else:
                f.write(line)

# Problem 9: Write a function to get the size of a file.
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
    word_count = {}
    most_frequent = None
    max_count = 0

    with open(filename, 'r') as f:
        for line in f:
            words = line.strip().lower().split()  # Convert to lowercase and split line into words
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1  # Increment word count

                # Update most frequent word if current word's count is higher
                if word_count[word] > max_count:
                    max_count = word_count[word]
                    most_frequent = word

    return most_frequent


# Problem 10: Write a function to create a file with N lines of numbers from 1 to N.
def create_file_with_numbers(filename, N):
    with open(filename, 'w') as f:
        for i in range(1, N+1):
            f.write(str(i) + '\n')


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
    total_words = 0
    total_length = 0
    
    with open(filename, 'r') as f:
        for line in f:
            words = line.strip().split()  # Split line into words
            total_words += len(words)
            total_length += sum(len(word) for word in words)

    return total_length / total_words if total_words else 0
