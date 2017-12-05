# CODEBY Python Challenge
# Second task
# Author: ETERN4L

# -*- coding: utf-8 -*-

def main():
    with open("text.txt", "r") as file:
        text = file.read().strip().split()
    for counter, word in enumerate(text):
        if word.isalpha():
            if len(word) > 6:
                text[counter] = word.capitalize()
        else:
            if len(word) > 7:
                text[counter] = word.capitalize()
    result = " ".join(text)
    with open("text.txt", "w") as file:
        file.write(result)
    return "Done! Now you can check some changes."

if __name__ == "__main__":
    try:
        print(main())
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt...")
    finally:
        input()
