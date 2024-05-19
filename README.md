# Raspberry Pi Configuration Scripts

This repository contains Python scripts for configuring a Raspberry Pi. Each script serves a specific purpose related to system configuration and GPIO setup.

## Script Descriptions:

### 1. configure_gpiomem.py

This script changes the ownership and permissions of the `/dev/gpiomem` device file. This step is necessary to allow access to GPIO pins without requiring root privileges. It ensures smoother interaction with GPIO peripherals.

Usage:
```bash
sudo python3 configure_gpiomem.py

2. configure_hdmi.py
This script updates HDMI settings in the /boot/config.txt file. It enables HDMI hotplug and sets the HDMI output to group 2, mode 51 (1920x1080 @ 60Hz). After applying the changes, it initiates a system reboot to ensure the new settings take effect.
sudo python3 configure_hdmi.py


3. start_pigpiod.py
This script starts the pigpiod daemon, a background process necessary for using the pigpio library in Raspberry Pi GPIO programming. Running this script is essential before attempting to control GPIO pins using pigpio.


sudo python3 start_pigpiod.py

Prerequisites:
Ensure that Python 3 is installed on your Raspberry Pi.
Run the scripts with superuser privileges (using sudo) to perform system-level tasks.
