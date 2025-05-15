import os
import platform
import socket
import subprocess

def run_command(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True)
    except subprocess.CalledProcessError as e:
        return str(e)

def check_interface():
    print("\n📡 Checking network interface...")
    system = platform.system()
    if system == "Windows":
        output = run_command("netsh wlan show interfaces")
        print(output)
    elif system == "Linux" or system == "Darwin":
        output = run_command("iwconfig")
        print(output)
    else:
        print("Unsupported OS.")

def check_ip_config():
    print("\n🌐 Checking IP configuration...")
    if platform.system() == "Windows":
        output = run_command("ipconfig")
    else:
        output = run_command("ifconfig")
    print(output)

def check_gateway_ping():
    print("\n📶 Pinging default gateway...")
    if platform.system() == "Windows":
        gateway = run_command("ipconfig | findstr /i 'Default Gateway'").split()[-1]
    else:
        gateway = run_command("ip route | grep default").split()[2]
    print(f"Default Gateway: {gateway}")
    response = run_command(f"ping -c 4 {gateway}" if platform.system() != "Windows" else f"ping -n 4 {gateway}")
    print(response)

def check_dns():
    print("\n🧭 Testing DNS resolution...")
    try:
        socket.gethostbyname("google.com")
        print("✅ DNS resolution is working.")
    except socket.error:
        print("❌ DNS resolution failed.")

def check_internet():
    print("\n🌍 Checking internet access (ping google.com)...")
    cmd = "ping -n 4 google.com" if platform.system() == "Windows" else "ping -c 4 google.com"
    result = run_command(cmd)
    print(result)

def main():
    print("=== Wi-Fi Troubleshooting Tool ===")
    check_interface()
    check_ip_config()
    check_gateway_ping()
    check_dns()
    check_internet()
    print("=== Diagnostic Complete ===\n")

if __name__ == "__main__":
    main()
