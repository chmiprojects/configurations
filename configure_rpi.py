import subprocess

def run_command(command):
    """Run a shell command."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the command: {e}")

def main():
    # Commands to change ownership and permissions of /dev/gpiomem
    commands = [
        "sudo chown root.gpio /dev/gpiomem",
        "sudo chmod g+rw /dev/gpiomem"
    ]

    for cmd in commands:
        run_command(cmd)

if __name__ == "__main__":
    main()
