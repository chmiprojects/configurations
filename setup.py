import subprocess

# Define the command to be executed
command = ["ls", "-l"]

# Execute the command
result = subprocess.run(command, capture_output=True, text=True)

# Print the command output
print(result.stdout)
