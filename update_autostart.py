import subprocess

def run_command(command):
    """Run a shell command."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the command: {e}")

def append_to_autostart():
    """Append a line to the autostart file."""
    autostart_file = "/etc/xdg/lxsession/LXDE-pi/autostart"
    line_to_add = '@lxterminal --command="~/autostart_program.sh"'
    
    try:
        with open(autostart_file, 'a') as file:
            file.write(f"\n{line_to_add}\n")
        print(f"Successfully added line to {autostart_file}")
    except Exception as e:
        print(f"An error occurred while updating the autostart file: {e}")

def main():
    # Ensure the script to be executed is executable
    run_command("sudo chmod +x ~/autostart.sh")
    
    # Append the line to the autostart file
    append_to_autostart()

if __name__ == "__main__":
    main()
