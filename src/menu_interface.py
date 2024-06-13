import time
from src.getch import get_arrow_key

def display_menu(links):
    current_index = 0

    def print_menu():
        print("\033c", end="")  # Clear the terminal
        print("Use the UP and DOWN arrow keys to navigate. Press ENTER to select.\n")
        for index, text, href in links:
            if index == current_index:
                print(f"> {text}")
            else:
                print(f"  {text}")

    print_menu()

    while True:
        key = get_arrow_key()
        if key == '[A' and current_index > 0:  # Up arrow key
            current_index -= 1
            print_menu()
        elif key == '[B' and current_index < len(links) - 1:  # Down arrow key
            current_index += 1
            print_menu()
        elif key in ('\n', '\r'):  # Enter key
            print(f"\nYou selected: {links[current_index][0]} - {links[current_index][1]}")
            return links[current_index][0]
        time.sleep(0.1)  # Debounce delay