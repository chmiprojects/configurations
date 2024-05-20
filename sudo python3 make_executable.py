import subprocess

def run_command(command):
    """Run a shell command."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the command: {e}")

def main():
    # Command to make autostart_program.sh executable
    run_command("sudo chmod +x autostart_program.sh")

if __name__ == "__main__":
    main()

