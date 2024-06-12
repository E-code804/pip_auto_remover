import pkg_resources
import os

# Outputs the number of packages required by
pkg = "numpy"
'''print(len(pkg_resources.get_distribution(pkg).requires()))

# Create a txt file with all downloaded packages.
os.system("pip list > pip_packages.txt")
# Shows details about a pkg
os.system(f"pip show {pkg}")'''

# Storing the result of a command.
command = f"pip show {pkg}"
# os.system(command)
# Capture the output of the command using subprocess.
result = os.popen(command).read()  # Result is now a string.
print("Output from command:", result.split("\n")[-2])

# Reading all the lines from the file with all downloaded packages.
with open("pip_packages.txt", "r") as f:
    packages = f.readlines()[2:]

# Display each package.
for package in packages:
    first_space = package.index(' ')
    curr_package = package[: first_space]
    result = os.popen(command).read()  # Result is now a string.
    print(curr_package)
    print("Output from command:", result.split("\n")[-2])