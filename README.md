# Quizz-Game
## 🧠 Quiz Game with Dataset Support
A command-line Python quiz game that dynamically loads questions from a CSV dataset file. Great for general knowledge quizzes, subject-specific tests, and educational purposes.

## 🎮 Features
Supports any number of multiple-choice questions (A/B/C/D).

Loads questions from a CSV file.

Real-time score tracking.

Colorful command-line interface using colorama.

Easy to expand with new topics or datasets.

## 📁 Dataset Format
The CSV file should follow this column structure:

question,optionA,optionB,optionC,optionD,answer
What is the capital of France?,London,Berlin,Paris,Rome,C
Who discovered gravity?,Newton,Einstein,Galileo,Kepler,A
The answer column should contain one of A, B, C, or D.

## 🚀 How to Run
Install dependencies (optional, if not installed):

pip install pandas colorama
Run the script:

python quiz_game.py
Provide the full path to your quiz CSV file when prompted, for example:

C:\Users\YourName\Documents\science_quiz.csv
## 📌 Example

🎓 Welcome to the Dataset-Based Quiz Game!

Q1: What is the capital of France?
A) London
B) Berlin
C) Paris
D) Rome
Your answer (A/B/C/D): C
✅ Correct!
## 📦 Files
quiz_game.py – Main Python script.

your_quiz.csv – CSV dataset with your quiz questions.

README.md – Project documentation.

## 💡 Customization
You can create different quizzes by saving new CSV files:

science_quiz.csv

history_quiz.csv

tech_quiz.csv

Just update the file path when launching the game.
