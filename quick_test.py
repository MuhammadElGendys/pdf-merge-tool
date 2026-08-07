# from main import PathValidation

# ui_input = input("pls enter path")
# result = PathValidation()

# reading files names save it in array and print it:

file_list = []

import os

#path = "/home/gt/Desktop/python"
path = input("add the path here: ")
for file in [pdf for pdf in os.listdir(path)
if pdf.endswith(".pdf")]:

  file_list.append(file)

for i in range(len(file_list)):
#Works fine till here when printing the file names
  print (file_list[i])
