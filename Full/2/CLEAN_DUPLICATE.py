import hashlib
import colorama
import tkinter
from tkinter import *
from tkinter import filedialog, messagebox
from collections import OrderedDict
from re import compile
import time
import os
import ctypes
from time import sleep
from datetime import datetime
root = tkinter.Tk()
root.withdraw()
print("Choose the input folder with format [Username]:[Password]:")
fileNameCombo = filedialog.askopenfile(parent=root, mode='rb', title='Choose your combo',filetype=(("txt", "*.txt"), ("All files", "*.txt")))
if fileNameCombo is None:
      print()
      print(Fore.RED + "Please select valid combo file!")
      time.sleep(2)
      sys.exit()
else:
      try:
            InFile = open(fileNameCombo.name, 'r+', encoding='utf-8')
      except Exception:
            print(Fore.RED + "Your input is dogshit, try again")
            time.sleep(2)
# path of the input and output files
print(fileNameCombo.name)
InFile = fileNameCombo.name
OutFile = "output.txt"
# holding the line which is already seen
lines_present = set()
# opening the output file in write mode to write in it
The_Output_File = open(OutFile, "w" , encoding='utf-8')

# loop for opening the file in read mode

for l in open(InFile, "r", encoding='utf-8'):
   # finding the hash value of the current line
      # Before performing the hash, we remove any blank spaces and new lines from the end of the line.
      # Using hashlib library determine the hash value of a line.
      hash_value = hashlib.md5(l.rstrip().encode('utf-8')).hexdigest()
      if hash_value not in lines_present:
         The_Output_File.write(l)
         lines_present.add(hash_value)
# closing the output text file
The_Output_File.close()
print("Operation complete close in 5s")
time.sleep(5)

