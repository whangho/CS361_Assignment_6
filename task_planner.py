# Author: Howard Whang
# OSU Email Address: whangho@oregonstate.edu
# Class: CS361
# Description: Sprint 1 - Develop the first 3 backlog items for my project.
# This project is to create a list or note-taking application. The goals for this sprint are to implement "Add To List",
# "Create New List", and "Remove from List" functions.


"""Global Variables"""
# Create master list. Contains the names of the lists that user creates.
master_list_names = []
# Create master list. Contains the data in the lists the user creates.
master_list_lists = []

def run_program():
    """Start Program. User can choose to start a new list, view the existing lists that have been
    created, view all the stored items at once, or remove a list in its entirety."""

    print("Hello! Welcome to A Very Mediocre To-Do List app! Please type one of these options:")
    print("<Start New List> <View Existing Lists> <View All Stored Items> <Remove List>")
    desired_task = input()

    # Create a new list #
    if desired_task.casefold() == "start new list":
        print("What will you name this list?")
        list_name = input()
        master_list_names.append(list_name)
        print("You have created a list:", list_name)
        saved_name_of_list = list_name
        list_name = []
        master_list_lists.append(list_name)

        # Does user want to add items to the newly created list? #
        # Yes, go to add_to_list(). No, go to run_program(). #
        loop_flag = False
        print("Do you want to add items to this list? Type <Yes> or <No>.")
        response = input()
        while loop_flag is False:
            if response.casefold() == "yes":
                loop_flag = True
                add_to_list(saved_name_of_list)
            elif response.casefold() == "no":
                loop_flag = True
                run_program()
            else:
                print("Sorry, invalid input. Please type <Yes> or <No>.")
                response = input()

    # View the current lists that the user has created #
    elif desired_task.casefold() == "view existing lists":
        print("Here are the lists you currently have:")
        print(master_list_names)

        # Does user want to open one of the lists? #
        # Yes, go to view_list(). No, go to run_program() #
        print("Do you want to open a list? Please type <Yes> or <No>.")
        response = input()
        loop_flag = False
        while loop_flag is False:
            if response.casefold() == "yes":
                loop_flag = True
                print("Which list do you want to open? Please type the name of the list. (This is case sensitive.)")
                list_to_open = input()
                if list_to_open in master_list_names:
                    view_list(list_to_open)
                else:
                    print("Sorry, that list does not exist.")
                    run_program()
            elif response.casefold() == "no":
                loop_flag = True
                run_program()
            else:
                print("Sorry, invalid input. Please type <Yes> or <No>.")
                response = input()

    # Print all items stored by the user. This will print the list #
    # of lists, as well as the contents of each list. #
    elif desired_task.casefold() == "view all stored items":
        print("Here are all the lists you have:", master_list_names)
        print("Here are all the contents of those lists:", master_list_lists)
        run_program()

    # Remove a list in its entirety #
    elif desired_task.casefold() == "remove list":
        print(master_list_names)
        print("Which list do you want to remove? Please type the name of the list. (This is case sensitive.)")
        list_to_delete = input()
        if list_to_delete in master_list_names:
            index = master_list_names.index(list_to_delete)
            master_list_names.remove(list_to_delete)
            master_list_lists.pop(index)
            print(list_to_delete, "has been removed.")
            run_program()
        else:
            print("Sorry, that list does not exist.")
            run_program()

    else:
        # RECURRRRSIOONNNNNNNNNNNNN
        print("Sorry, invalid input.")
        run_program()


def view_list(name_of_list):
    """Open a list for viewing."""
    index = master_list_names.index(name_of_list)
    print(master_list_lists[index])

    # Does user want to add to the list? Yes, go to add_to_list(). #
    # No, ask if user would like to remove from list. #
    loop_flag = False
    print("Do you want to add items to this list? Type <Yes> or <No>.")
    response = input()
    while loop_flag is False:
        if response.casefold() == "yes":
            loop_flag = True
            add_to_list(name_of_list)
        elif response.casefold() == "no":
            loop_flag = True
            print("Do you want to remove items from this list? Type <Yes> or <No>.")
            # If yes, go to remove_from_list(). #
            # If no, go to run_program(). #
            response_2 = input()
            loop_flag_2 = False
            while loop_flag_2 is False:
                if response_2.casefold() == "yes":
                    loop_flag_2 = True
                    remove_from_list(name_of_list)
                elif response_2.casefold() == "no":
                    loop_flag_2 = True
                    run_program()
                else:
                    print("Sorry, invalid input. Please type <Yes> or <No>.")
                    response_2 = input()
        else:
            print("Sorry, invalid input. Please type <Yes> or <No>.")
            response = input()


def add_to_list(name_of_list):
    """Allows user to add new items to a particular list. The name of the list must be given to this function."""
    index = master_list_names.index(name_of_list)
    print("Type what you want to add to this list:")
    note_item = input()
    master_list_lists[index].append(note_item)
    print("Item added to list.")
    print("Continue adding to this list? Type <Yes> or <No>.")
    response = input()
    loop_flag = False
    while loop_flag is False:
        if response.casefold() == "yes":
            loop_flag = True
            add_to_list(name_of_list)
        elif response.casefold() == "no":
            loop_flag = True
            run_program()
        else:
            print("Sorry, invalid input. Please type <Yes> or <No>.")
            response = input()


def remove_from_list(name_of_list):
    """Removes an item from a particular list. The name of the list must be given to this function."""
    index = master_list_names.index(name_of_list)
    loop_flag = False
    while loop_flag is False:
        print("Type what you want to remove from the list: (This is case sensitive.)")
        item_to_remove = input()
        if item_to_remove in master_list_lists[index]:
            loop_flag = True
            master_list_lists[index].remove(item_to_remove)
            print(item_to_remove, "was deleted.")
            run_program()
        else:
            print("Sorry, that is not an item in the list.")


# Run The Program
run_program()