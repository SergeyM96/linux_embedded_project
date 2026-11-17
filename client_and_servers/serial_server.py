import sys
import serial

DEVICE = sys.argv[1] if len(sys.argv) > 1 else "/dev/ttyAMA0"
BAUD = 115200   # for a real board

def main():
    with serial.Serial(DEVICE, BAUD, timeout=None) as ser: # open a serial connection
        print(f"serial echo on {DEVICE} @ {BAUD}", flush=True) # flush sends text out right away instead of it sitting in a buffer
        try:
            while True:
                data = ser.read(1)                 # block until the first byte arrives
                data += ser.read(ser.in_waiting)   # + whatever else is already waiting
                ser.write(data.upper())            # write() sends everything
        except KeyboardInterrupt:
            print("\nstopped")


if __name__ == "__main__":
    main()