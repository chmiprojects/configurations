import subprocess

def run_command(command):
    """Run a shell command."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the command: {e}")

def main():
    # Command to start pigpiod daemon
    run_command("sudo pigpiod")

if __name__ == "__main__":
    main()
