import platform
import subprocess
import shutil
import socket
import os
from datetime import datetime

# global list to store log data
report_data = []

def log_and_print(text):
    print(text)
    report_data.append(text)

def print_header(title):
    log_and_print(f"\n--- {title} ---")

def check_system():
    print_header("system info")
    log_and_print(f"os: {platform.system().lower()} {platform.release().lower()}")
    log_and_print(f"architecture: {platform.machine().lower()}")

def check_disk():
    print_header("disk usage (system drive)")
    # set path based on os
    path = "c:\\" if platform.system().lower() == "windows" else "/"
    total, used, free = shutil.disk_usage(path)
    
    log_and_print(f"drive: {path.lower()}")
    log_and_print(f"total: {total // (2**30)} gb")
    log_and_print(f"used:  {used // (2**30)} gb")
    log_and_print(f"free:  {free // (2**30)} gb")

def check_internet():
    print_header("network connectivity (dns ping)")
    # windows uses -n, unix/linux uses -c
    ping_flag = "-n" if platform.system().lower() == "windows" else "-c"
    
    try:
        # silent ping to google servers
        subprocess.check_call(
            ["ping", ping_flag, "1", "8.8.8.8"], 
            stdout=subprocess.DEVNULL, 
            stderr=subprocess.STDOUT
        )
        log_and_print("status: connected (ping to 8.8.8.8 successful)")
    except subprocess.CalledProcessError:
        log_and_print("status: disconnected (ping failed)")

def get_local_ip():
    print_header("local ip address")
    try:
        # dummy udp connection to get our own local ip
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        log_and_print(f"ip: {ip}")
    except Exception:
        log_and_print("ip: unable to determine")

def save_report():
    print_header("report generation")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"diagnostic_report_{timestamp}.txt"
    
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("\n".join(report_data))
        print(f"[+] report saved to file: {filename}")
    except Exception as e:
        print(f"[-] failed to save report: {e}")

if __name__ == "__main__":
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_and_print(f"starting it support diagnostic tool at {timestamp}...\n")
    
    check_system()
    check_disk()
    check_internet()
    get_local_ip()
    
    save_report()
    print("\ndiagnostics complete.")