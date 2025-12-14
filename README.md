# 🧠 QuizApp – Console Quiz Application
🎓 Programming Foundations – FHNW, BSc BIT

A console-based quiz application written in Python.  
The project demonstrates fundamental programming concepts such as console interaction, data validation, loops, functions, and file processing.
---
## 📝 Analysis

### Problem

In many learning situations, students want a simple way to test their knowledge and receive immediate feedback.  
Manual quizzes or paper-based tests are time-consuming and do not provide instant evaluation or grading.

This application solves the problem by providing an automated quiz system that presents questions, validates answers, and calculates a final grade.

---

### Scenario

The quiz app is used in a console environment.  
A user starts the program, answers multiple-choice questions, receives immediate feedback for each answer, and sees a final score and grade at the end of the quiz.

### User Stories

- As a user, I want to answer quiz questions in the console.
- As a user, I want to choose my answer using numbers.
- As a user, I want to know immediately if my answer is correct or wrong.
- As a user, I want to see the correct answer if I was wrong.
- As a user, I want to receive a final grade after completing the quiz.

---

### Use Cases

- Load quiz questions from a JSON file
- Display questions and answer options
- Validate user input
- Check answers and count correct responses
- Calculate and display a final grade

---

## ✅ Project Requirements

Each app must fulfill the following criteria:

### 1. Interactive App (Console Input)

The application interacts with the user through the console. Users can:

- Enter their answers using numeric input
- Progress through multiple questions
- Receive feedback after each answer
- See a final result and grade

---

### 2. Data Validation

The application validates all user input to prevent errors and crashes:

- User input is checked to ensure it is numeric
- Input values are validated to be within the available answer range
- Invalid input results in a warning message and a retry

This ensures a smooth user experience and meets the validation requirements of the module.

---

### 3. File Processing

The application uses file processing to manage quiz data:

**Input file:**  
`questions.json` — Contains all quiz questions, answer options, and the correct answer index.

Example:

json
{
  "question": "What is Python?",
  "options": ["A snake", "A programming language", "A database"],
  "correct_index": 1
}

---

✅ Project Requirements
Each app must meet the following three criteria in order to be accepted (see also the official project guidelines PDF on Moodle):

Interactive app (console input)
Data validation (input checking)
File processing (read/write)

---

### 📄 `README.md` – Teil 10 (Team, Highlights, License)

md
## 👥 Team & Contributions

| Name | Contribution |
|------|-------------|
| Noel | Creating the JSON file and loading questions |
| Josh | Grade calculation and answer checking |
| Lars | Loops, input validation, and final output |

## ⭐ Highlights

- Platform-independent file handling
- Clean separation of logic using functions
- Stable input validation without program crashes
- Clear and fair grading system


---

## 🗂️ Getting the project to work
-Download the python and Json file
-Make sure they are in the same folder
-Make sure the json file is called questions.json

