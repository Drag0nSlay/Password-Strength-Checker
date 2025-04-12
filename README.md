# Password Strength Checker (CLI + GUI)

A cybersecurity-focused internship project by **Aman Kothari** that evaluates password strength through two modes:
- A fast **Command Line Interface (CLI)** tool
- A user-friendly **Graphical User Interface (GUI)** built with **CustomTkinter**

---

## Features

- Rates password strength as **Weak**, **Moderate**, or **Strong**
- GUI supports dark/light mode with CustomTkinter theme
- CLI version is lightweight and quick to use
- Custom validation rules can be extended
- Secure and private – no data is stored or shared

### CLI Version
- Checks password strength based on:
  - Length
  - Use of uppercase, lowercase, digits, special characters
  - Presence in **rockyou.txt** (common passwords list)
- Simple and fast to use in terminal

### GUI Version (CustomTkinter)
- Show/Hide password toggle
- One-click **Copy** to clipboard
- Option to **Save report** as `password_report.txt`
- Suggests a strong password automatically
- Dark/light theme support

---

## Project Structure
```
password-strength-checker/
│
├── cli_version/
│   └── password_checker_cli.py           # CLI implementation
│
├── gui_version/
│   └── password_checker_gui.py           # GUI implementation using CustomTkinter
│
├── assets/
│   └── screenshot.png                    # Optional: GUI preview or branding image
│
├── LICENSE                               # Strict copyright license
├── requirements.txt                      # Dependencies for both versions
└── README.md                             # Project overview and instructions
```
---

## How to Use

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run CLI Version
```bash
cd cli_version
python password_checker_cli.py
```

### 3. Run GUI Version
```bash
cd gui_version
python password_checker_gui.py
```

## Author
Aman Kothari(Drag0nSlay)
CyberSecurity Intern at Hack Secure
![LinkedIN][def]

[def]: https://www.linkedin.com/in/aman-kothari-995944274/
