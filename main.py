# libraries imported
import os


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
user_input_files_number = input("Please enter the PDFs number: ")

# loop to open each single file
for i in range(user_input_files_number):
    temp_file_concatenation = user_input_path + i + ".pdf"
    with open(temp_file_concatenation, mode="r", encoding="utf-8") as file:
        content = file.read()
