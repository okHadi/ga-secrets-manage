import os

lines_to_check = []  # List to store line numbers containing 'jobs:' keyword

def process_file(file_path):
    # Open the file and read its contents
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Find the line number where 'jobs:' is present
        for line_number, line in enumerate(lines, start=1):
            if "jobs:" in line:
                jobs_line_number = line_number
                break

        # Store the lines starting from the 'jobs:' line until the end
        job_lines = lines[jobs_line_number:]

        # Iterate through the lines and check for specific conditions
        for x in range(len(job_lines)):
            if len(job_lines[x]) == len(job_lines[x].strip()) + 3:
                # Check if the line length is equal to the stripped line length + 3
                # (2 spaces are added and one space is default in all lines)
                lines_to_check.append(jobs_line_number + x)

        # Iterate through the identified lines and perform further checks
        for j in range(len(lines_to_check)):
            if "prod" in lines[lines_to_check[j] + 1]:
                continue  # Skip if 'prod' is present in the next line

            # Check for 'secrets.AWS_PROD_ACCESS' in the subsequent lines
            elif j != len(lines_to_check) - 1:
                for k in range(lines_to_check[j] + 1, lines_to_check[j + 1]):
                    if "secrets.AWS_PROD_ACCESS" in lines[k]:
                        raise Exception("ERROR: Production secret found in non-prod job")
            else:
                for l in range(lines_to_check[j] + 1, len(lines)):
                    if "secrets.AWS_PROD_ACCESS" in lines[l]:
                        raise Exception("ERROR: Production secret found in non-prod job")


folder_path = ".github\\workflows"

# Iterate through the folder and process each file
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".yml"):
            file_path = os.path.join(root, file)
            process_file(file_path)
