import platform
import subprocess
import shutil
import socket

def print_header(title):
    print(f"\n--- {title} ---")

def check_system():
    print_header("system info")
    # returns darwin for mac, windows for pc
    print(f"os: {platform.system().lower()} {platform.release().lower()}")
    print(f"architecture: {platform.machine().lower()}")

def check_disk():
    print_header("disk usage (root /)")
    # shutil gets disk data, divide by 2**30 to convert bytes to gb
    total, used, free = shutil.disk_usage("/")
    print(f"total: {total // (2**30)} gb")
    print(f"used:  {used // (2**30)} gb")
    print(f"free:  {free // (2**30)} gb")

def check_internet():
    print_header("network connectivity (dns ping)")
    # silent ping to google servers. -c 1 means 1 packet.
    try:
        subprocess.check_output(["ping", "-c", "1", "8.8.8.8"], stderr=subprocess.STDOUT)
        print("status: connected (ping to 8.8.8.8 successful)")
    except subprocess.CalledProcessError:
        print("status: disconnected (ping failed)")

def get_local_ip():
    print_header("local ip address")
    try:
        # dummy udp connection to get our own local ip
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        print(f"ip: {ip}")
    except Exception:
        print("ip: unable to determine")

if __name__ == "__main__":
    print("starting it support diagnostic tool...")
    check_system()
    check_disk()
    check_internet()
    get_local_ip()
    print("\ndiagnostics complete.")