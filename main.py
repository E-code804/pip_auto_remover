import pkg_resources
import os

# Create a txt file with all downloaded packages.
os.system("pip list > pip_packages.txt")

# Reading all the lines from the file with all downloaded packages.
with open("pip_packages.txt", "r") as f:
    packages = f.readlines()[2:]

with open("non_requiredby.txt", "w+") as f:
    # Display each package.
    for package in packages:
        first_space = package.index(' ')
        curr_package = package[: first_space]
        command = f"pip show {curr_package}"
        result = os.popen(command).read()  # Result is now a string.
        print(curr_package)
        required_by = result.split("\n")[-2]
        if len(required_by) == 13:
            f.write(curr_package + "\n")
