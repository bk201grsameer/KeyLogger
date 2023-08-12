Sure, here's a basic Markdown file outlining the key features and usage of your keylogger program:

```markdown
# Keylogger Program

This is a simple keylogger program written in Python using the pynput library to capture keyboard events. The program runs a keylogger in a separate thread and allows users to interact with it through commands in the main thread.

## Features

- Captures keyboard events (key presses) in the background.
- Displays captured keylog data upon user request.
- Provides a command to terminate the keylogger thread safely.

## Requirements

- Python 3.x
- pynput library (`pip install pynput`)
- termcolor library (`pip install termcolor`)
- Colors module (assuming it's part of your project)

## Usage

1. Make sure you have Python installed on your system.

2. Install the required libraries using the following commands:
   ```
   pip install pynput termcolor
   ```

3. Create a Python file and copy the provided keylogger code into it.

4. Run the program using the command:
   ```
   python your_keylogger_program.py
   ```

5. Follow the instructions displayed in the terminal:
   - The program starts a keylogger thread.
   - You can use the "dump log" command to display captured keystrokes.
   - To safely terminate the keylogger thread, use the "quit" command.

6. The keylogger thread will be gracefully terminated, and the program will exit.

## Disclaimer

**Note:** This program is intended for educational purposes only. Please use it responsibly and with the appropriate permissions. Unauthorized use of keyloggers is illegal and unethical.

## Author

- Your Name
- Contact: your.email@example.com
```

Replace `your_keylogger_program.py`, `Your Name`, and `your.email@example.com` with appropriate values. Additionally, make sure to include any additional information or details specific to your project.