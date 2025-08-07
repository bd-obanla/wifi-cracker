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
sudo apt update
sudo apt install aircrack-ng network-manager python3

## Usage
- sudo python3 wifi-cracker.py

## Legal Warning
- Use this tool only on networks you own or have permission to test. Unauthorized use is illegal.
