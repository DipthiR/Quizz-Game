import pandas as pd
from colorama import Fore, Style, init
import time
import os

init(autoreset=True)

def load_questions(file_path):
    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError("File does not exist at the provided path.")
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(Fore.RED + f"❌ Error loading file: {e}")
        return None

def run_quiz(data):
    score = 0
    print(Fore.CYAN + Style.BRIGHT + "\n🎓 Welcome to the Dataset-Based Quiz Game!\n")
    time.sleep(1)

    for index, row in data.iterrows():
        print(Fore.YELLOW + f"Q{index+1}: {row['question']}")
        print(Fore.BLUE + f"A) {row['optionA']}")
        print(Fore.BLUE + f"B) {row['optionB']}")
        print(Fore.BLUE + f"C) {row['optionC']}")
        print(Fore.BLUE + f"D) {row['optionD']}")

        user_ans = input(Fore.GREEN + "Your answer (A/B/C/D): ").strip().upper()

        if user_ans == row['answer'].strip().upper():
            print(Fore.GREEN + "✅ Correct!\n")
            score += 1
        else:
            print(Fore.RED + f"❌ Wrong! Correct answer: {row['answer'].upper()}\n")
        time.sleep(0.8)

    print(Fore.MAGENTA + f"\n📊 Your final score: {score} out of {len(data)}")

def main():
    file_path = input("Enter the full path to your quiz CSV file: ").strip()
    data = load_questions(file_path)
    if data is not None:
        run_quiz(data)

if __name__ == "__main__":
    main()
