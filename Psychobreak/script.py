import os
import subprocess

random_path = "/tmp/temp/random.dic"

with open(random_path, "r") as file:
    for word in file.readlines():
        word = word.strip()
        subprocess.call(["./program", word])
        #print(word)
