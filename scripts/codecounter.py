import os

print("Welcome to code counter!")
print("------------------------")

file_extension = input("Give the file extension you want to count: ")

print("Your choice is: " + file_extension)

confirm_extension = input("Do you want to continue (y/n): ")

print("------------------------")

if confirm_extension == "y":

    for file in os.listdir(os.getcwd()):
        
        if file.endswith(file_extension):
            
            with open(file, "r") as f:

                for line in f:

                    content = f.read()
                    counter = 0
                    line = line.strip(os.linesep)

                    for i in line:
                        if i:
                            counter += 1

                    print("Lines:")
                    print(counter)

        else:
            print("ERROR: No files with the given extension were found from this directory")
            break

else:
    print("Code counter exited")