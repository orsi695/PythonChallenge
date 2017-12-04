# CODEBY Python Challenge
# First task
# Author: ETERN4L

def main():
    try:
        digit = int(input("Please, input a integer: "))
        if digit % 3 == 0:
            print(True)
        else:
            print(False)
    except:
        print("Unexpected error! Please, try again.")
    finally:
        input()

if __name__ == "__main__":
    main()
