import socket

def receive_report(ip_address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip_address, port))
    sock.listen(1)
    conn, addr = sock.accept()
    report = conn.recv(1024).decode()
    with open('server_report.txt', 'w') as f:
        f.write(report)
    conn.close()

if __name__ == '__main__':
    ip_address = "185.100.54.38"  # Replace with the IP address of this server
    port = 4444  # Replace with the port number to use
    receive_report(ip_address, port)