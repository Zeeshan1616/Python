<div align="center">

# 🔐 Password Strength Checker

### A Python CLI tool that scores your password and tells you exactly how to make it stronger
</div>

---

## 📖 Overview

**Password Strength Checker** is a lightweight, menu-free command-line tool that analyzes any password you enter and rates it on a **5-star scale**. It checks length, character variety, digits, and special characters — then gives instant, emoji-driven feedback on what's missing and what's solid.

No dependencies. No setup. Just run it and check your password in seconds.

---

## ✨ Features

| Check | What it looks for |
|---|---|
| 📏 **Length** | At least 8 characters |
| 🔠 **Uppercase** | At least one uppercase letter |
| 🔡 **Lowercase** | At least one lowercase letter |
| 🔢 **Digits** | At least one number (without being *only* numbers) |
| 🔣 **Special Characters** | At least one of `! @ # $ % ^ & *` |
| ⭐ **Strength Rating** | Final score from 1–5 stars based on conditions met |

---

## 🖥️ Demo

```
Welcome To Password Strength Checker 💗
Enter a password here: Passw0rd!

✅ The length of the password is Acceptable
✅ The uppercase condition is satisfied
✅ The lowercase condition is satisfied
✅ The password is Alphanumeric
✅ The password contains Special characters 

⭐⭐⭐⭐⭐
⚠ Password Strength: Strong
```

---

## ⚙️ How It Works

The script runs **5 independent checks** on the input password, each contributing one point (`satisfied`) toward the final strength score:

1. **Length check** — password must be `>= 8` characters
2. **Case check** — loops through each character with `.isupper()` / tracks lowercase count
3. **Digit check** — loops through each character with `.isnumeric()`, ensuring digits exist *without* being purely numeric
4. **Special character check** — scans for `!  @  #  $  %  ^  &  *`
5. **Final score** — `satisfied` (0–5) maps to a star rating and strength label:

| Satisfied Conditions | Rating | Strength |
|:---:|:---:|:---|
| 1 | ⭐ | Weak |
| 2 | ⭐⭐ | Weak – Medium |
| 3 | ⭐⭐⭐ | Medium |
| 4 | ⭐⭐⭐⭐ | Medium – Strong |
| 5 | ⭐⭐⭐⭐⭐ | Strong |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed

### Run it

```bash
git clone https://github.com/your-username/password-strength-checker.git
cd password-strength-checker
python password_checker.py
```

Then just type a password when prompted — instant feedback follows.

---

## 🗂️ Project Structure

```
password-strength-checker/
│
├── password_checker.py     # Main script
└── README.md                # You're here
```

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:** None — pure Python, zero dependencies

---

## 🔮 Roadmap

- [ ] Add password entropy calculation
- [ ] Support checking multiple passwords in one run
- [ ] Export strength report to a file
- [ ] Add a GUI version (Tkinter)

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo, open an issue, or submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

<div align="center">

### 👨‍💻 Author

**Zeeshan**
Computer Systems Engineering @ Mehran UET, Jamshoro


⭐ If you found this useful, consider giving it a star!

</div>
