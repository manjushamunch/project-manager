def get_project_information():
    print("Please provide the following project information:")
    project_id = input("Project ID: ")
    project_name = input("Project Name: ")
    start_date = input("Start Date: ")
    expected_finish_date = input("Expected Finish Date: ")
    first_name = input("Project Manager First Name: ")
    last_name = input("Project Manager Last Name: ")
    phone = input("Project Manager Phone: ")
    email = input("Project Manager Email: ")

    return {
        "Project ID": project_id,
        "Project Name": project_name,
        "Start Date": start_date,
        "Expected Finish Date": expected_finish_date,
        "Project Manager First Name": first_name,
        "Project Manager Last Name": last_name,
        "Project Manager Phone": phone,
        "Project Manager Email": email
    }

def save_to_file(project_info):
    folder_name = "data"
    filename = f"{folder_name}/{project_info['Project ID']}.txt"
    with open(filename, "w") as file:
        file.write("Project Details:\n")
        for key, value in project_info.items():
            file.write(f"{key}: {value}\n")
        file.write("\n")
