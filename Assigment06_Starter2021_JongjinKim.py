# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Jongjin Kim,11/22/2021,Modified code to complete assignment 06
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection

# Processing  --------------------------------------------------------------- #


class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": str(task).strip(), "Priority": str(priority).strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        # TODO: Add header and code Here!
        print("Remove a new item fro the list/Table")
        for row in list_of_rows:
            print(row["Task"] + "," + row["Priority"].strip())
        for row in list_of_rows:
            if row["Task"].lower() == task.lower():
                table_lst.remove(row)
                print("A selected task removed!")
        return list_of_rows, 'success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        # TODO: Add header and code Here!
        print("Save Data to File")
        file = open(file_name, "w")
        for row in list_of_rows:
            file.write(row["Task"] + "," + row["Priority"] + "\n")
        file.close()
        print("Data saved in '" + file_name + "' !")
        return list_of_rows, 'success'


def add_data_to_list(task, priority, list_of_rows):
    # TODO: Add header and code Here!
    print("Add header and data")
    row_dic = {"Task": str(task).strip(), "Priority": str(priority).strip()}
    list_of_rows.append(row_dic)
    # print list to check
    for row in list_of_rows:
        print(row["Task"], ",", row["Priority"])
    return list_of_rows, 'success'

# Presentation (Input/Output)  -------------------------------------------- #
#table_lst = [{"Task":"Lamp", "Priority":20}, {"Task":"Desk", "Priority":100}]
stritem = ""
strvalue = ""


class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_task_and_priority():
        pass  # TODO: Add header and code Here!
        stritem = str(input("What is the item? - ")).strip()
        strvalue = str(input("What is the value? - ")).strip()
        print()
        return stritem, strvalue
        #return task, priority

    @staticmethod
    def input_task_to_remove():
        pass  # TODO: Add header and code Here!
        stritem = str(input("What item do you want to remove? - ")).strip()
        print(stritem)
        return stritem


# Main Body of Script  ------------------------------------------------------ #
table_lst, status = Processor.read_data_from_file(file_name_str, table_lst)
print(table_lst)
print(status)
if status == 'success':
    # test add data
    table_lst, status = add_data_to_list("Lamp", 200, table_lst)
    print(table_lst)
    print(status)

    if status == 'success':
        # test remove data
        table_lst, status = Processor.remove_data_from_list("Lamp", table_lst)
        print(table_lst)
        print(status)

        if status == 'success':
            # test write data
            table_lst, status = Processor.write_data_to_file(file_name_str, table_lst)
            print(table_lst)
            print(status)

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name_str, table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.output_current_tasks_in_list(table_lst)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task
        # TODO: Add Code Here
        print("Add a new Task")
        strItem, strValue = IO.input_new_task_and_priority()
        print(strItem, strValue)
        if status == 'success':
            print("Done!")
        table_lst, status = add_data_to_list(strItem, strValue, table_lst)
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Task
        # TODO: Add Code Here
        print("Remove an existing Task")
        strItem = IO.input_task_to_remove()
        table_lst, status = Processor.remove_data_from_list(strItem, table_lst)
        if status == 'success':
            print("Done!")
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        # TODO: Add Code Here
        print("Save Data to file")
        table_lst, status = Processor.write_data_to_file(file_name_str, table_lst)
        if status == 'success':
            print("Done!")
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # and Exit
