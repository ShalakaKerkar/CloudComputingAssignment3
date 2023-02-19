import os
import re
import socket
from collections import Counter

with open("/home/data/IF.txt") as file:
    if_content = file.read()
with open("/home/data/Limerick-1.txt") as file:
    limerick_content = file.read()
print("Contents of IF.txt:")
print(if_content)
print("\nContents of Limerick-1.txt:")
print(limerick_content)
text_files = [f for f in os.listdir("/home/data/") if f.endswith(".txt")]
print("Text files in /home/data/assignment3:", text_files)
word_counts = {}
for filename in text_files:
    with open(os.path.join("/home/data/", filename)) as file:
        contents = file.read()
        words = re.findall(r'\b\w+\b', contents)
        word_counts[filename] = len(words)
print("Number of words", word_counts)

grand_total = sum(word_counts.values())
print("Grand total of words:", grand_total)
def get_top_n_words(file_path, n=3):
    with open(file_path, 'r') as f:
        contents = f.read()
        words = re.findall(r'\w+', contents)
        word_counts = Counter(words)
        return word_counts.most_common(n)

if_file_path = os.path.join('/home/data/', "IF.txt")
top_3_words = get_top_n_words(if_file_path)
print(f"The top 3 words in {if_file_path} are:")
for word, count in top_3_words:
    print(f"{word}: {count}")
ip_address = socket.gethostbyname(socket.gethostname())
print("IP address of the machine:", ip_address)
output_filename = "/home/data/result.txt"
with open(output_filename, "w") as file:
    file.write("Text files in /home/data: " + str(text_files) + "\n")
    file.write("Grand total of words: " + str(grand_total) + "\n")
    file.write("Top 3 words in IF.txt: " + str(top_3_words) + "\n")
    file.write("Number of words  " + str(word_counts) + "\n")
    file.write("IP address of the machine: " + str(ip_address) + "\n")

with open(output_filename) as file:
    result = file.read()
print(result)
