[README.md](https://github.com/user-attachments/files/30067652/README.md)
# Password Strength Analyzer

## Project Description

Password Strength Analyzer is a web-based application developed using Python and Flask. It evaluates the strength of user-entered passwords based on length, complexity, uniqueness, and entropy. The application also suggests stronger passwords and prevents users from reusing previously saved passwords using a SQLite database.

---

## Features

- Check password strength
- Check password length
- Verify uppercase, lowercase, numbers, and special characters
- Calculate password entropy
- Suggest improvements for weak passwords
- Generate a strong random password
- Prevent reuse of previously used passwords
- Web dashboard using Flask
- Live password strength meter using JavaScript

---

## Technologies Used

- Python 3
- Flask
- HTML5
- CSS3
- JavaScript
- SQLite

---

## Project Structure


PasswordStrengthAnalyzer/
│
├── app.py
├── main.py
├── password_checker.py
├── password_generator.py
├── database.py
├── passwords.db
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md


---

## Installation

1. Clone or download the project.

2. Open the project in Visual Studio Code.

3. Install Flask:


pip install flask


4. Run the application:


python app.py


5. Open your browser and visit:


http://127.0.0.1:5000


---

## How It Works

1. Enter a password.
2. The application checks:
   - Password length
   - Uppercase letters
   - Lowercase letters
   - Numbers
   - Special characters
   - Password entropy
3. The application displays:
   - Password score
   - Password strength
   - Suggestions for improvement
   - Generated strong password
4. Previously used passwords are detected using the SQLite database.

---

## Expected Output

- Password Strength (Weak / Medium / Strong / Very Strong)
- Password Score
- Password Entropy
- Suggestions
- Generated Strong Password

---

## Future Enhancements

- Integration with Have I Been Pwned API
- User login system
- Password history management
- Export report as PDF

