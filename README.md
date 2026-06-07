# IT Support Toolkit

A lightweight CLI tool designed for quick, automated system and network diagnostics. Built entirely with Python's standard library, requiring no external dependencies.

## What does this script do?

The script performs automated checks to assist with Level 1 IT Support troubleshooting:
* **System Info:** Retrieves basic operating system and architecture details.
* **Disk Usage:** Calculates total, used, and free space on the root drive.
* **Network Connectivity:** Verifies internet access by pinging Google's DNS (8.8.8.8).
* **Local IP:** Resolves and displays the machine's local IP address on the network.

## How to run it?

1. Open the terminal in the project folder.
2. Run the script directly (no virtual environment or external libraries required): 
   `python3 diag.py`