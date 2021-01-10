"""
Name: Saikiran Rudra
Topic: Sach Educational Support Tasks
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Task 1. Python code to create matrix using for loop with example.
def task_1():
    # 1. Input matrix dimension from user
    no_of_rows = int(input("Enter number of rows: "))
    no_of_columns = int(input("Enter number of cols: "))

    # initializing matrix
    matrix = []

    # Input values to the matrix (row by row)
    for row in range(1, no_of_rows + 1):  # nrow + 1 because range fn doesn't consider upper bound
        column_values = input(f"Enter {row}st row values values should be space separated e.g 1 2 3: ").split(" ")

        # converting list of strings to integer because input returns string
        column_values = [int(value) for value in column_values]

        # check weather user have enter valid number of row values
        if len(column_values) != no_of_columns:
            # if number of values entered is invalid exit code with error message
            print("❌ Invalid no of values try again")
            return

        # if input values is of valid dimension add it to matrix
        matrix.append(column_values)

    # Printing Generated Matrix
    print(matrix)


# Task 2. Python code to Press enter key using selenium with detailed explanation
# I am using chrome driver for this task we have other options as well
# lets open google.com for this task and search some thing and press enter
DRIVER_PATH = "./chromedriver.exe"


def task_2():
    # Initialising chrome web driver of selenium
    with webdriver.Chrome(executable_path=DRIVER_PATH) as wd:
        # opening google.com
        wd.get("https://images.google.com/")
        # Selecting search bar
        search_bar = wd.find_elements_by_class_name("gLFyf")[0]
        # Entering a search term
        search_bar.send_keys("Sach Educational Support")
        # Pressing Enter (OBJECTIVE OF TASK 2)
        search_bar.send_keys(Keys.ENTER)


if __name__ == "__main__":
    task_1()
    task_2()
