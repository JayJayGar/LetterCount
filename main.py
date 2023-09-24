import re

def counting_letters(file_path):
    try:
        with open(file_path, 'r') as file:
            # Initialize a dictionary to store letter counts
            letter_counts = {}
            # Define a regular expression pattern for Latin letters
            latinChar = re.compile(r'[a-zA-Z]')

            for line in file:
                # Convert everything into lowercase
                line = line.lower()
                for char in line:
                    # Check if the character is a Latin letter
                    if latinChar.match(char):
                        # Increment the count for the letter in the dictionary
                        letter_counts[char] = letter_counts.get(char, 0) + 1
            # Print the letter counts
            for letter, count in sorted(letter_counts.items()):
                print(f'{letter}: {count}')

    except FileNotFoundError:
        print(f'The file "{file_path}" was not found.')
    except Exception as e:
        print(f'An error occurred: {e}')

file_path = 'gettysburg.txt'
counting_letters(file_path)