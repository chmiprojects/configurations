import subprocess
import sys

def install_package(package_name):
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', 'install', package_name], check=True, capture_output=True, text=True)
        print(f"Package {package_name} installed successfully")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to install package {package_name}")
        print(e.stdout)
        print(e.stderr)

packages = ['customtkinter', 'RPi.GPIO', 'ultralytics', 'pigpio', 'CTkMessagebox']

for package in packages:
    install_package(package)

