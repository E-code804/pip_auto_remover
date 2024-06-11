import pkg_resources
import os

# Outputs the number of packages required by
pkg = "numpy"
print(len(pkg_resources.get_distribution(pkg).requires()))

# Create a txt file with all downloaded packages.
os.system("pip list > pip_packages.txt")
# Shows details about a pkg
os.system(f"pip show {pkg}")

# Storing the result of a command.
command = "echo Hello, World!"
os.system(command)
# Capture the output of the command using subprocess.
result = os.popen(command).read() # Result is now a string.
print("Output from command:", result[0])
