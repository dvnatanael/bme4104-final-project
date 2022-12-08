import os
import re
import sys
import termios
import time
import tty

import serial


def getkey():
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    try:
        while True:
            b = os.read(sys.stdin.fileno(), 3).decode()
            if len(b) == 3:
                k = ord(b[2])
            else:
                k = ord(b[0])
            key_mapping = {
                127: "backspace",
                10: "return",
                32: "space",
                9: "tab",
                27: "esc",
                65: "up",
                66: "down",
                67: "right",
                68: "left",
            }
            return key_mapping.get(k, chr(k))
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)


def read_input_buffer():
    while ser.in_waiting:
        input_buffer = ser.readline().decode().strip()
        print(input_buffer)


if __name__ == "__main__":
    arduino_port = (
        f"/dev/{[dev for dev in os.listdir('/dev') if re.search(r'(ACM|AMA)', dev)][0]}"
    )
    print(f"Using port: {arduino_port}")
    baud_rate = 9600
    ser = serial.Serial(arduino_port, baud_rate)

    try:
        while True:
            k = getkey()
            if k == "esc":
                quit()
            elif k == "w":
                ser.write(b"forward\n")
            elif k == "s":
                ser.write(b"backward\n")
            elif k == "a":
                ser.write(b"left\n")
            elif k == "d":
                ser.write(b"right\n")
            elif k == "x":
                ser.write(b"stop\n")
            elif k == "q":
                ser.write(b"open\n")
            elif k == "e":
                ser.write(b"close\n")
            elif k == "f":
                ser.write(b"temperature\n")
                ser.reset_input_buffer()
                time.sleep(10)
                read_input_buffer()
            elif k == "space":
                print("picture")
            else:
                print(k)

            time.sleep(0.05)
            read_input_buffer()
    except (KeyboardInterrupt, SystemExit):
        ser.write(b"stop\n")
    except ser.SerialException:
        pass
    finally:
        os.system("stty sane")
        print("stopping.")
