import argparse
import socket
import time
import requests
import serial

HOST = "192.168.0.2"
TCP_PORT, HTTP_PORT, SERIAL_PORT = 5000, 5001, 5002
TIMEOUT = 3

def call_tcp():
    with socket.create_connection((HOST, TCP_PORT), timeout=TIMEOUT) as sock:
        sock.sendall(b"hello")
        return sock.recv(1024).decode()

def call_serial():
    with serial.serial_for_url(f"socket://127.0.0.1:{SERIAL_PORT}", timeout=TIMEOUT) as ser:
        ser.write(b"hello")
        return ser.read(1024).decode()

def call_http():
    response = requests.get(f"http://{HOST}:{HTTP_PORT}/alive", timeout=TIMEOUT)
    return response.text

CHANNELS = {"tcp": call_tcp, "serial": call_serial, "http": call_http}

def main():
    parser = argparse.ArgumentParser(description="Client for calling different types of services")
    parser.add_argument("--interval", type=float, default=1.0, help="Interval between calls in seconds")
    parser.add_argument("--channel", choices=CHANNELS, default="tcp")
    args = parser.parse_args()

    func = CHANNELS[args.channel]
    try:
        while True:
            try:
                print(func())
            except Exception as e:         
                print("error:", e)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("Interrupted")             

if __name__ == "__main__":
    main()