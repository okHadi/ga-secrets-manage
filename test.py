import os

jobsLineNo = None

endingLine = None
linesArr = []
def process_file(file_path):
    # Replace this with the code you want to perform on each file
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, start=1):
            if "jobs:" in line:
                jobsLineNo = line_number
                break
    with open(file_path, 'r') as file:
        
        startingLine = 0
        lines = file.readlines()
        jobLines = lines[jobsLineNo:]
        #print(jobLines)
        for x in range(len(jobLines)):
            print("line:",jobLines[x])
            print("line length:",len(jobLines[x]))
            print("line after strip:", jobLines[x].strip())
            print("line after strip length:", len(jobLines[x].strip()))
            print("--------------------")
            if (len(jobLines[x]) == len(jobLines[x].strip())+3): #+3, because 2 spaces are added and one space is default in all lines.
                   linesArr.append(jobsLineNo+x+1)
                   continue



                

# Replace "folder_path" with the actual path to the ".github" folder
folder_path = ".github\\workflows"



for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".yml"):
            file_path = os.path.join(root, file)
            process_file(file_path)
            print(linesArr)

