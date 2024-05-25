import subprocess
import os

# Define the paths and content
script_path = '/autostart_program.sh'
line_to_add = '"python3 /main.py"\n'



def add_lines_to_rc_local(rc_local_path="/etc/rc.local", lines_to_add=None):
    if lines_to_add is None:
        lines_to_add = [
            "sudo chown root.gpio /dev/gpiomem &",
            "sudo chmod g+rw /dev/gpiomem &",
            "sudo pigpiod &"
        ]
    
    try:
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
    
    except Exception as e:
        print(f"An error occurred: {e}")


# Step 1: Create or update the shell script
def create_or_update_shell_script():
    try:
        # Read the file and check if the line is already present
        with open(script_path, 'r') as file:
            lines = file.readlines()

        if line_to_add not in lines:
            # Append the line to the file
            with open(script_path, 'a') as file:
                file.write(line_to_add)
            print(f'Line "{line_to_add.strip()}" added to {script_path}.')
        else:
            print(f'Line "{line_to_add.strip()}" already present in {script_path}.')
    except FileNotFoundError:
        # If file does not exist, create it and add the line
        with open(script_path, 'w') as file:
            file.write('#!/bin/bash\n')
            file.write(line_to_add)
        print(f'File {script_path} created with the line "{line_to_add.strip()}".')

    # Make the script executable
    subprocess.run(['chmod', '+x', script_path], check=True)
    print(f'{script_path} is now executable.')

# Step 2: Add to LXDE autostart
def add_to_lxde_autostart():
    autostart_path = '/etc/xdg/lxsession/LXDE-pi/autostart'
    autostart_line = f'@lxterminal --command=/autostart_program.sh\n'
    
    try:
        with open(autostart_path, 'r') as file:
            lines = file.readlines()
        
        if autostart_line not in lines:
            with open(autostart_path, 'a') as file:
                file.write(autostart_line)
            print(f'Line "{autostart_line.strip()}" added to {autostart_path}.')
        else:
            print(f'Line "{autostart_line.strip()}" already present in {autostart_path}.')
    except FileNotFoundError:
        with open(autostart_path, 'w') as file:
            file.write(autostart_line)
        print(f'File {autostart_path} created with the line "{autostart_line.strip()}".')

if __name__ == '__main__':
    create_or_update_shell_script()
    add_to_lxde_autostart()
    add_lines_to_rc_local()
