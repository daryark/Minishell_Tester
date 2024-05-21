import os
import sys
import signal


def send_signal(pid, message):
    # check if pid is valid
    try:
        os.kill(pid, 0)
    except OSError:
        print(f"Invalid PID: {pid}")
        sys.exit(1)

    with open("/tmp/signal_data.txt", "w") as file:
        file.write(message)

    os.kill(pid, signal.SIGUSR1)
    print(message)

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("Usage: python3 client.py <PID> <'string to send'>")
        sys.exit(1)
    else:
        pid = int(sys.argv[1])
        message = sys.argv[2]
        send_signal(pid, message)
    