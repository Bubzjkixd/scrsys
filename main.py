import os
import sys


directory_input = sys.argv[1]
list_dir = os.listdir(directory_input)


for number, directory in enumerate(list_dir):
    print(f"{number}. : {directory}")
print(f"Le contenu de mon répertoire : {list_dir}")