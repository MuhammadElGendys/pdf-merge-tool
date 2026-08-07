# libraries imported
from pypdf import PdfReader as PR
from pypdf import PdfWriter as PW
import os
import re

# functions

def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else 0

def LongSeparetor():
    print("========================================================")

def MidSeparetor():
    print("============================")

def ShortSeparetor():
    print("==============")

def PathValidation(path):
    while((path == "") | (not os.path.exists(path))):
        path = input("Path is empty or doesn't exist - please try again: ")
    return path

def GetUserInput():
    global user_input_path
    global pdf_list
    user_input_path = input("Please enter the folder's path: ")
    user_input_path = PathValidation(user_input_path)
    pdf_list = []

    for file in [pdf for pdf in os.listdir(user_input_path)
    if pdf.endswith(".pdf")]:
        pdf_list.append(file)
    pdf_list.sort(key=extract_number)
    # printing test
    # for i in range(len(pdf_list)):
    #     print (pdf_list[i])

def MergingPDFs():
    merge = PW()
    for pdf in pdf_list:
        pdf_path = os.path.join(user_input_path, pdf)
        merge.append(pdf_path)
    merge.write(os.path.join(user_input_path, "merged.pdf"))

def InitText():
    LongSeparetor()
    print("N.B.: The order of your PDFs should be like: 0, 1, 2...")
    LongSeparetor()

try:
    InitText()
    GetUserInput()
    MergingPDFs()
except Exception as e:
    print(f"Something went wrong: {e}")