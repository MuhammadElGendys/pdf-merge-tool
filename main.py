# libraries imported
from pypdf import PdfReader as PR
from pypdf import PdfWriter as PW

# functions
def LongSeparetor():
    print("========================================================")

def MidSeparetor():
    print("============================")

def ShortSeparetor():
    print("==============")

LongSeparetor()
print("N.B.: The order of your PDFs should be like: 0, 1, 2...")
LongSeparetor()

user_input_path = input("Please enter the folder's path: ")
user_input_files_number = int(input("Please enter the PDFs number: "))

# loop to open each single file
for i in range(user_input_files_number):
    pass