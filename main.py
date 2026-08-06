# libraries imported
from pypdf import PdfReader as PR
from pypdf import PdfWriter as PW
import os

# functions
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
    user_input_path = input("Please enter the folder's path: ")
    user_input_path = PathValidation(user_input_path)
    global user_input_files_number
    user_input_files_number = int(input("Please enter the PDFs number: "))

def ReadingPDFs():
    # loop to open each single file
    for i in range():
        pass

def InitText():
    LongSeparetor()
    print("N.B.: The order of your PDFs should be like: 0, 1, 2...")
    LongSeparetor()

GetUserInput()
