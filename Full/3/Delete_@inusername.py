import os
import re
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
      print("Please select valid combo file!")
      time.sleep(2)
      sys.exit()
else:
      try:
            InFile = open(fileNameCombo.name, 'r+', encoding='utf-8')
      except Exception:
            print("Your input is dogshit, try again")
            time.sleep(2)
# path of the input and output files
print(fileNameCombo.name)
InFile = fileNameCombo.name
OutFile = "output.txt"
print("fuck")

file1 = open(f"{InFile}", 'r+', encoding='utf-8')
lines = file1.readlines()
res = ''
x = 0
for line in lines:
    username = line.split(":")[0].replace('\n', '')
    password = line.split(":")[1].replace('\n', '')
    if username.isalnum() != True:
        x += 1
    else:
        if len(username) >= 6 and username != 'UNKNOWN':
            euwrite = open(f"{OutFile}", "a+", encoding='utf-8')
            euwrite.write(f"{line}")
            euwrite.close
print("done")
print("Operation complete close in 5s")
time.sleep(5)
        

