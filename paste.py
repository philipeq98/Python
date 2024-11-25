import pyperclip
import pyautogui
import time

def paste_clipboard_to_textbox():
    # Give the user time to select the textbox
    print("You have 3 seconds to select the textbox...")
    time.sleep(3)

    # Get the text from the clipboard
    clipboard_text = pyperclip.paste()

    # Paste the clipboard text into the selected textbox
    pyautogui.write(clipboard_text)

# Call the function
paste_clipboard_to_textbox()
