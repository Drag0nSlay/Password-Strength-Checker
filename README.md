# Password Strength Checker (CLI + GUI)

A cybersecurity-focused internship project by **Aman Kothari** that evaluates password strength through two modes:
- A fast **Command Line Interface (CLI)** tool
- A user-friendly **Graphical User Interface (GUI)** built with **CustomTkinter**
> This project showcases the work done as part of the internship program offered by **@Hack Secure**.
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
> **Note:** This project uses `rockyou.txt` to detect weak/common passwords.
> Due to its large size (~14MB), it is **not included** in this repository.
> Please download it manually and place it in the same directory as the script to enable full functionality.

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
├── cli/
│   └── cli.py           # CLI implementation
│
├── gui/
│   └── gui.py           # GUI implementation using CustomTkinter
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
python cli.py
```

### 3. Run GUI Version
```bash
cd gui_version
python gui.py
```
## Screenshots
![GUI Screenshot](assets/password_gui.png)
![CLI Screenshot](assets/password_cli.png)
![Report Screenshot](assets/password_report.png)
## Author
Aman Kothari(Drag0nSlay)<br>
CyberSecurity Intern at Hack Secure<br>
[LinkedIn](https://www.linkedin.com/in/aman-kothari-995944274/)
