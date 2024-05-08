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
print("Choose the input folder with format:")
folderName = filedialog.askdirectory(parent=root, title='Choose your combo')
print(folderName)
if folderName is None:
      print()
      print("Please select valid folder!")
      time.sleep(2)
      sys.exit()
else:
      print("Load done")
      print(folderName)
# path of the input and output files

InFile = folderName
res = []
print(InFile)
for root, dirs, files in os.walk(InFile):
    for file in files:
        if file.endswith(".txt"):
            res.append(os.path.join(root, file))
print("Loading Res")
            
filename = input('Type in password file name correctly(password.txt, passwords.txt, Passwords.txt,...): ')
usernameformat = input('Type in username format correctly(Username: , login: , USER: , LOGIN: ,...): ')
passwordformat = input('Type in password format correctly(Password: , pass: , PASS: , PASS: ,...): ')
print(filename)
for lines in res:
    if lines.find(filename) != -1:
        print(lines)
        file1 = open(f"{lines}", 'r+', encoding='utf-8')
        content = file1.readlines()
        result_string = ''
        cnt = 0
        for line in content:
            if line.find(usernameformat) != -1:
                username = line
                cnt += 1
                if cnt == 2:
                    result_string = ''
                    result_string += username.strip() + ':'
                    cnt = 1
                else:
                    result_string += username.strip() + ':'
            else:
                if line.find(passwordformat) != -1:
                    password = line
                    if result_string == '':
                        result_string += 'default:'
                        result_string += password.strip()
                    else:
                        result_string += password.strip()
                    result_string = result_string.replace(usernameformat, '')
                    result_string = result_string.replace(passwordformat, '')
                    euwrite = open(f"output.txt", "a+", encoding='utf-8')
                    euwrite.write(f"{result_string}\n")
                    euwrite.close
                    result_string = ''
                    cnt = 0
print("Operation complete close in 5s")
time.sleep(5)

                
        
        


