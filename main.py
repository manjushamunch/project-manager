import os
from functions import get_project_information
from functions import save_to_file

project_details = []


def add_project_details():
    # Function to add project details, validate uniqueness, and manager's name and email
    print("Add Project details")
    # Get the information
    project_info = get_project_information()

    # Save collected information to file named after Project ID
    save_to_file(project_info)
    pass

def read_project_details():
    # Function to read project details from a file
    print("Read Project details")
    pass

def save_entries():
    # Function to save entries to a file
    print("Save entries")
    pass

def remove_entries():
    # Function to remove entries from the file if they exist
    print("Remove entries")
    pass

def update_project_details():
    # Function to update existing project details
    print("Update existing project details")
    pass

def search_projects():
    # Function to search for projects
    print("Search for Projects")
    pass

def print_all_project_details():
    # Function to print all project details
    print("Print all Project details")
    pass

def validate_manager(manager_name, manager_email):
    # Function to validate manager name and email
    pass

def sort_entries():
    # Function to sort entries
    pass

def show_menu():
    print("Menu:")
    print("1. Add Project details")
    print("2. Read Project details")
    print("3. Save entries")
    print("4. Remove entries")
    print("5. Update existing project details")
    print("6. Search for Projects")
    print("7. Print all Project details")
    print("8. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_project_details()
        elif choice == '2':
            read_project_details()
        elif choice == '3':
            save_entries()
        elif choice == '4':
            remove_entries()
        elif choice == '5':
            update_project_details()
        elif choice == '6':
            search_projects()
        elif choice == '7':
            print_all_project_details()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
