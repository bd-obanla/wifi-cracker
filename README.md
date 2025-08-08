# WiFi Cracker
A Python script to scan WiFi networks, attempt to crack passwords, and connect automatically.

## Features
- Scans for available WiFi networks using `nmcli`.
- Attempts to crack WPA/WPA2 passwords with `aircrack-ng`.
- Automatically connects to networks with found passwords.

## Prerequisites
- Linux system (e.g., Kali Linux, Ubuntu)
- Tools: `nmcli`, `aircrack-ng`
- Python 3
- A compatible wireless adapter supporting monitor mode

## Installation
```bash
# Update the package list
sudo apt update

# Install required tools and Git
sudo apt install aircrack-ng network-manager python3 git -y

# Clone the repository
git clone https://github.com/bd-obanla/wifi-cracker.git

# Navigate to the project directory
cd wifi-cracker

# Make the script executable
chmod +x wifi_cracker.py

# Check your wireless interface (replace wlan0 with your interface if different)
iwconfig

# Start monitor mode on your wireless interface (replace wlan0 with your interface)
sudo airmon-ng start wlan0

# Run the script (use sudo for network privileges)
sudo python3 wifi_cracker.py
