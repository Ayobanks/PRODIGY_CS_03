🔐 Password Strength Checker

This is a simple Python tool that assesses the strength of a password based on the following criteria:

- Length of the password
- Use of uppercase and lowercase letters
- Inclusion of numbers
- Presence of special characters (e.g., !, @, #, etc.)

The program provides real-time feedback to users on whether their password is Weak, Okay, or Strong, and gives suggestions for improvement.

📂 Project Structure
password_checker/
│
├── password_checker.py   # Main Python script
└── README.md             # Project description and instructions

▶️ How to Use
Clone or download the repository.
Open a terminal and navigate to the project directory.
Run the script using Python:

python password_checker.py

Enter your password when prompted.

The program will analyze it and display feedback.

✅ Strength Criteria
Strength Level	Requirements
Weak	Password is less than 8 characters long, or only contains one type of character (e.g., all lowercase or only digits).
Okay	Password is 8–12 characters long and includes a mix of uppercase, lowercase, and numbers.
Strong	Password is more than 12 characters long and contains uppercase letters, lowercase letters, numbers, and symbols.


👩‍💻 Author
Made with ❤️ by AyoBanks
