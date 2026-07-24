# 🎓 Student Manager

A simple, interactive command-line application built in Python for managing a list of students. It allows users to add, remove, search, sort, and display student records — all through an easy-to-use text menu.

```
========================================
.....Welcome to the Student Manager.....
========================================
```

## ✨ Features

- **➕ Add Student** — Add one or multiple students to the list in a single session.
- **➖ Remove Student** — Search for and remove a student by name, with a confirmation prompt.
- **🔍 Search Student** — Find a student and get their position (index) in the list.
- **📋 Display All Students** — View the complete, numbered list of all students.
- **🔤 Sort Students** — Sort the list alphabetically (A–Z) or reverse the current order.
- **🔢 Total Student Count** — Quickly check how many students are currently in the list.
- **🚪 Exit** — Cleanly exit the application.

## 🖥️ Requirements

- Python 3.x (no external libraries required — uses only the Python standard library)

## 🚀 Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/student-manager.git
   cd student-manager
   ```

2. Run the script:
   ```bash
   python student_manager.py
   ```

## 📖 Usage

When you run the program, you'll be presented with a menu:

```
Choose the option form bellow:
1. Add Student
2. Remove Student
3. Search Student
4. Display All Student
5. Sort Student
6. total Student
7. Exit
```

Simply enter the number corresponding to the action you'd like to perform, and follow the on-screen prompts. Most options let you repeat the action (e.g., adding several students in a row) by answering `y` when asked "Do you want to do this again?".

### Example Session

```
Choose from 1-7: 1

Enter the name of Student you want to add: alice
Alice  has been added to the student list :)

Do you want to add another student (y/n): n

Choose from 1-7: 4
Here is the entire list of students:

          1 . Alice
Do you want to display all the students again? (y/n): n
```

> **Note:** Student names are automatically capitalized (e.g., `alice` becomes `Alice`) for consistency.

## 🗂️ Menu Reference

| Option | Action              | Description                                             |
|:------:|----------------------|----------------------------------------------------------|
| 1      | Add Student          | Adds a new student to the list                          |
| 2      | Remove Student       | Removes an existing student after confirmation           |
| 3      | Search Student       | Finds a student and shows their list index                |
| 4      | Display All Student  | Prints the full, numbered student list                   |
| 5      | Sort Student         | Sorts alphabetically or reverses the list order           |
| 6      | Total Student        | Displays the current number of students                  |
| 7      | Exit                 | Closes the application                                   |

## 🛠️ Possible Improvements

This project is intentionally simple and beginner-friendly. Some ideas for future enhancements:

- Persist data to a file or database (e.g., JSON, CSV, SQLite) so records survive between runs.
- Store additional student details (roll number, grade, contact info) instead of just names.
- Handle duplicate names more gracefully (e.g., using unique IDs).
- Add input validation for empty or invalid entries.
- Write unit tests for core operations (add, remove, search, sort).

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues) or submit a pull request.

---

Made with ❤️ using Python.
