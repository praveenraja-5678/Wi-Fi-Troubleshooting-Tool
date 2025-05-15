# Wi-Fi-Troubleshooting-Tool

📘 Documentation: Wi-Fi Troubleshooting Tool

📝 Overview

The Wi-Fi Troubleshooting Tool is a cross-platform Python command-line utility designed to assist users and support engineers in identifying common Wi-Fi and internet connectivity problems. It runs a series of checks and displays the results with diagnostic feedback.

📦 System Requirements

Component	Requirement

Language	Python 3.x

OS	Windows,Linux, macOS (basic)

Libraries	Built-in (os, platform, subprocess, socket)

🔧 Installation

Clone or download the repository:

bash

https://github.com/praveenraja-5678/Wi-Fi-Troubleshooting-Tool.git

cd Wi-Fi Troubleshooting

No dependencies required.

🚀 How to Run

bash

python wifi_kit.py

You must run the script from a terminal or command prompt with Python installed.

🔍 Features

Feature	Description

Wi-Fi Interface Check	Identifies current connection and interface signal strength

IP Configuration	Displays IPv4 address, subnet mask, gateway, and DNS servers

Gateway Ping	Tests reachability of the default gateway

DNS Resolution Check	Resolves google.com to test DNS server response

Internet Connectivity Check	Pings Google to test full internet access

🖥️ Platform-Specific Notes

✅ Windows:

Uses netsh wlan, ipconfig, and ping

Works on all modern versions (Windows 10+)

✅ Linux:

Uses iwconfig, ifconfig, and ip route

Requires basic net-tools package (for ifconfig)

✅ macOS:

iwconfig may not be available by default (use networksetup if needed)

📸 Sample Output

=== Wi-Fi Troubleshooting Tool ===

📡 Checking network interface...
SSID : OfficeWiFi
Signal : 89%
State : connected

🌐 Checking IP configuration...
IPv4 Address : 192.168.0.12
DNS Server : 1.1.1.1

📶 Pinging default gateway...
Reply from 192.168.0.1: time=3ms

🧭 Testing DNS resolution...
✅ DNS resolution is working.

🌍 Checking internet access...
Reply from google.com: time=18ms

=== Diagnostic Complete ===
🧪 Troubleshooting Scenarios Detected
Problem	Possible Message	Suggestion
No IP address	IP config shows no IPv4	Reconnect to Wi-Fi, reboot router
Gateway not reachable	Ping to gateway fails	Router may be down, check cables
DNS not resolving	DNS resolution failed	Try changing DNS to 8.8.8.8 or 1.1.1.1
Internet down	Google ping fails	ISP issue, check modem

📁 Project Files
File	Purpose
wifi_kit.py	Main script
README.md	Project overview
docs/	(Optional) Documentation folder
sample.log	(Optional) Output sample

📌 Roadmap / Future Features

Export results to .txt, .json, or .log file

Add retry/timeout logic to ping commands

Implement a GUI using Tkinter or PyQt

Auto-fix options (flush DNS, renew IP)

📄 License

This project is released under the MIT License. Feel free to modify and distribute.
