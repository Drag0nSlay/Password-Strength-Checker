import re
import os

rockyou = set()
rockyou_loaded = False

def load_rockyou():
    global rockyou, rockyou_loaded
    if os.path.exists("rockyou.txt"):
        try:
            with open("rockyou.txt", "r", encoding="latin-1", errors="ignore") as file:
                rockyou = set(line.strip().lower() for line in file if line.strip())
            rockyou_loaded = True
        except Exception as e:
            print("Error Loading rockyou.txt:", e)

def common_pass(pwd):
    return pwd.lower() in rockyou if rockyou_loaded else False

def check_password_strength(pwd):
    length = len(pwd)
    types = sum([
        bool(re.search(r'[A-Z]', pwd)),
        bool(re.search(r'[a-z]', pwd)),
        bool(re.search(r'\d', pwd)),
        bool(re.search(r'[^A-Za-z0-9]', pwd))
    ])

    if length < 6 or common_pass(pwd) or types < 2:
        return 'Weak'
    elif length >= 12 and types == 4:
        return 'Strong'
    else:
        return 'Moderate'

def main():
    load_rockyou()
    print("Password Strength Checker")
    print("-------------------------")
    while True:
        pwd = input("Enter Password or type 'exit': ")
        if pwd.lower() == 'exit':
            break
        result = check_password_strength(pwd)
        print(f"Strength: {result}\n")

if __name__ == '__main__':
    main()
