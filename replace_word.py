#!/usr/bin/python3

import os
import sys

word_old = sys.argv[1]
word_new = sys.argv[2]
file = sys.argv[3]

print(f"word_old: {word_old}")
print(f"word_new: {word_new}")

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

for root, dirs, files in os.walk(file):
    for f_name in files:
        f_path = os.path.join(root, f_name)
        print(f_path)
        try:
            with open(f_path, 'r') as f:
                content = f.read()
            indexs = findall(content, word_old)
            if indexs:
                with open(f_path, 'w') as f:
                    for start_index in indexs:
                        end_index = start_index + len(word_old)
                        new_content = content[:start_index] + word_new + content[end_index:]
                        content = new_content
                    f.write(new_content)
        except:
            pass



