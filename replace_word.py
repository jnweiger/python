#!/usr/bin/python3

import os
import sys

# get the OLD AND NEW WORD AND THE FILE PATH FROM COMMAND line arguments
word_old = sys.argv[1]
word_new = sys.argv[2]
file = sys.argv[3]

print(f"word_old: {word_old}")
print(f"word_new: {word_new}")

# function to find all occurrences of a word in a text
def findall(text, word):
    result = []
    last_idx = 0
    while True:
        start_idx = text.lower().find(word.lower(), last_idx)
        if start_idx < 0:
            break
        result.append(start_idx)
        last_idx = start_idx + len(word)
    return result

# iterate over all files in the directory tree rooted at the given file path
for root, dirs, files in os.walk(file):
    for f_name in files:
        f_path = os.path.join(root, f_name)
        print(f_path)
        try:
            # read the file content
            with open(f_path, 'r') as f:
                content = f.read()

            # find all occurrences of the old word in the file content
            indexs = findall(content, word_old)

            if indexs:
                # if the old word exists, replace it with the new word and write the new content back to the file
                with open(f_path, 'w') as f:
                    for start_index in indexs:
                        end_index = start_index + len(word_old)
                        new_content = content[:start_index] + word_new + content[end_index:]
                        content = new_content
                    f.write(new_content)

        except:
            # ignore any errors that occur while reading or writing a file
            pass



