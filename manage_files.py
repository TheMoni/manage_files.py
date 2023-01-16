# Importing needed libraries
from os.path import exists
import os


def read_data():  # Function for reading file contents
    filename = input("Enter file name: ")  # Getting filename

    if not exists("Database"):  # If directory "Database" does not exist create directory with name "Database"
        os.mkdir("Database")

    if not exists(f"Database\{filename}.txt"):  # If the file does not exist in directory "Database" then create file
        open(f"Database\{filename}.txt", "x")

    print("")

    f = open(f"Database\{filename}.txt", "r")   # Open file
    data = f.readline(50)  # Read the stored data

    if data == "":  # Check if file is empty
        print("File is empty!")
    else:
        print(data)  # Print the contents of the file


def write_data():  # Function for writing to a file
    print("")

    filename = input("Enter file name: ")

    if not exists("Database"):  # If directory "Database" does not exist create directory with name "Database"
        os.mkdir("Database")

    if not exists(f"Database\{filename}.txt"):  # If the file does not exist in directory "Database" then create file
        open(f"Database\{filename}.txt", "x")

    data = input("Enter data: ")
    f = open(f"Database\{filename}.txt", "r")

    data2 = str(f.readline(50))  # Read the currently stored data
    f2 = open(f"Database\{filename}.txt", "w")

    if data2 == "":  # Write data
        f2.writelines(str(f"{data}\n"))
    else:
        f2.writelines(f"{data2}\n")
        f2.writelines(str(f"{data}\n"))


def create_file():  # Function for creating a file
    if not exists("Database"):  # If directory "Database" does not exist create directory with name "Database"
        os.mkdir("Database")

    print("")
    filename = input("Enter file name: ")

    if not exists(f"Database\{filename}.txt"):  # If the file does not exist in directory "Database" then create file
        open(f"Database\{filename}.txt", "x")
    else:
        print("")
        print(f"File with the name {filename}.txt already exists!")  # If file already exists print error


def list_files():  # Function for listing files in a directory
    if not exists("Database"):  # If directory "Database" does not exist create directory with name "Database"
        os.mkdir("Database")

    data = os.listdir("Database")  # Get Files in directory
    print("")
    print("IF THE OUTPUT IS [] THEN THERE ARE NO FILES FOUND!")
    print("")
    print(data)  # Print files in directory


def delete_file():  # Function for deleting a file
    print("")

    filename = input("Enter file name: ")

    if not exists("Database"):  # If directory "Database" does not exist create directory with name "Database"
        os.mkdir("Database")

    print("")

    if exists(f"Database\{filename}.txt"):  # Check if file exists
        os.remove(f"Database\{filename}.txt")
        print(f"File with name {filename}.txt has been deleted!")
    else:
        print("File does not exist!")


def menu():  # Main Menu function
    print("")                                 # Main Menu Design
    print("        Made by TheMoni!")
    print("================================")
    print("          MANAGE FILES")
    print("")
    print("       1 - Write to file!")
    print("      2  - Read from file!")
    print("        3 - Create file!")
    print("        4 - Delete file!")
    print("        5 - List files!")
    print("")
    print("            0 - EXIT")
    print("================================")
    print("")

    user_input = int(input("Enter Option: "))  # Getting user input

    if user_input == 1:  # Checking which option the user chose
        write_data()
        menu()
    elif user_input == 2:
        read_data()
        menu()
    elif user_input == 3:
        create_file()
        menu()
    elif user_input == 4:
        delete_file()
        menu()
    elif user_input == 5:
        list_files()
        menu()
    elif user_input == 0:
        print("")
        print("Closing...")
    else:
        print("")
        print("No such option!")  # Print error if no such option exists
        menu()


menu()  # Running the main menu function
