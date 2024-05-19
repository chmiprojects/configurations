import subprocess

def run_command(command):
    """Run a shell command."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the command: {e}")

def main():
    # Commands to update HDMI settings
    commands = [
        "echo 'hdmi_force_hotplug=1' >> /boot/config.txt",
        "echo 'hdmi_group=2' >> /boot/config.txt",
        "echo 'hdmi_mode=51' >> /boot/config.txt",
        "sudo reboot"
    ]

    for cmd in commands:
        run_command(cmd)

if __name__ == "__main__":
    main()
