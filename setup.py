import os

# Path to rc.local
rc_local_path = "/etc/rc.local"

# Lines to add
lines_to_add = [
    "sudo chown root.gpio /dev/gpiomem &",
    "sudo chmod g+rw /dev/gpiomem &",
    "sudo pigpiod &"
]

# Read the current rc.local content
with open(rc_local_path, "r") as file:
    content = file.readlines()

# Check if each line to add already exists
lines_to_append = [line + "\n" for line in lines_to_add if line + "\n" not in content]

# If there are lines to append
if lines_to_append:
    # Find the index of "exit 0" line
    exit_index = next((i for i, line in enumerate(content) if line.strip() == "exit 0"), None)
    if exit_index is not None:
        # Insert the new lines before "exit 0"
        content = content[:exit_index] + lines_to_append + content[exit_index:]

        # Write the modified content back to rc.local
        with open(rc_local_path, "w") as file:
            file.writelines(content)

        print("New lines added to rc.local.")
    else:
        print("Couldn't find 'exit 0' line in rc.local. Lines not added.")
else:
    print("Lines already exist in rc.local. No changes needed.")
