# 🔐 Random Password Generator

## 📌 Project Description
The Random Password Generator is a Python-based command-line application that generates random passwords based on user-defined criteria.

Users can specify the password length and select different character types, including uppercase letters, lowercase letters, numbers, and symbols.

## 🎯 Objective
To develop a Python tool that generates strong random passwords while allowing users to customize password length and character combinations.

## 🛠️ Technologies Used
- Python 3
- Random Module
- String Module

## ✨ Features
- Generates random passwords.
- Minimum password length of 8 characters.
- Supports uppercase letters (A–Z).
- Supports lowercase letters (a–z).
- Supports numbers (0–9).
- Supports special symbols (!@#$%^&*).
- Allows users to select character types.
- Input validation for password length and character selection.
- Option to generate multiple passwords without restarting the program.

## 📂 Project Structure

```text
Python-Task3-Random Password Generator/
│
├── password_generator.py
│
└── README.md
```

## ▶️ How to Run the Project

**Step 1:** Install Python 3 on your computer.

**Step 2:** Clone or download this repository.

**Step 3:** Open the project folder in VS Code.

**Step 4:** Open the terminal.

**Step 5:** Run the following command:

```bash
python password_generator.py
```

## 💻 Sample Output

```text
===== RANDOM PASSWORD GENERATOR =====

Enter password length (minimum 8): 12

Select character types:
1. Uppercase Letters (A-Z)
2. Lowercase Letters (a-z)
3. Numbers (0-9)
4. Symbols (!@#$%^&*)

Enter your choices (e.g., 1234): 1234

Generated Password: A7@mK9#pL2$x

Generate another password? (yes/no): yes
```

## 📚 Learning Outcomes
- Understanding Python functions.
- Working with Python random and string modules.
- Using loops and conditional statements.
- Implementing input validation.
- Understanding random password generation.
- Improving problem-solving skills.

## 👨‍💻 Author
**Sourav NP**

B.Tech – Computer Science and Engineering

## 📌 Project Category
Python Programming – Beginner Level

## 🔒 Security Note
This beginner version uses Python's random module for password generation. For applications requiring real-world password security, Python's secrets module is recommended.
