quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "Rome", "Madrid"],
        "answer": 0  
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": 1  
    },
    {
        "question": "Which programming language is this?",
        "options": ["Java", "C++", "Python", "Ruby"],
        "answer": 2  
    }
]


def display_question(question_data, question_number):
    print(f"\nQuestion {question_number}: {question_data['question']}")
    for i, option in enumerate(question_data["options"]):
        print(f"  {i + 1}. {option}")
    return question_data["answer"]


def get_user_answer():
    while True:
        try:
            user_input = int(input("Your answer (1-4): ")) - 1
            if 0 <= user_input <= 3:
                return user_input
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")


def run_quiz():
    print("Welcome to the Quiz App!\n")
    score = 0

    for i, question_data in enumerate(quiz_data, start=1):
        correct_answer = display_question(question_data, i)
        user_answer = get_user_answer()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question_data['options'][correct_answer]}\n")

    print(f"Quiz Over! Your score: {score}/{len(quiz_data)}")
    if score == len(quiz_data):
        print("Congratulations! You got all answers correct!")
    elif score > len(quiz_data) // 2:
        print("Great job! Keep practicing to get a perfect score!")
    else:
        print("Better luck next time!")


if __name__ == "_main_":
    run_quiz()