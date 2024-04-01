import random

questions = {
    "What is the capital of France?": ["Paris", "London", "Berlin", "Rome"],
    "What is the capital of Germany?": ["Berlin", "London", "Paris", "Rome"],
    "What is the capital of Italy?": ["Rome", "London", "Berlin", "Paris"],
    "What is the capital of Spain?": ["Madrid", "London", "Berlin", "Paris"],
    "What is the capital of UK?": ["London", "Paris", "Berlin", "Rome"],
    "What is the capital of USA?": ["Washington", "Paris", "Berlin", "Rome"],
    "What is the capital of Japan?": ["Tokyo", "London", "Paris", "Rome"],
    "What is the capital of China?": ["Beijing", "London", "Berlin", "Paris"],
    "What is the capital of India?": ["New Delhi", "London", "Berlin", "Paris"],
    "What is the capital of Russia?": ["Moscow", "Paris", "Berlin", "Rome"]
}

score = 0
correct_answers = 0
wrong_answers = 0

# Select 10 random questions from the dictionary
selected_questions = random.sample(list(questions.items()), 10)

for question, options in selected_questions:
    print(question)
    correct_answer = options[0]  # Assign the first option as the correct answer
    random.shuffle(options)  # Shuffle the options
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    
    # Check if the user's answer is correct
    if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
        if options[int(user_answer) - 1] == correct_answer:
            print("Correct!")
            score += 1
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer.capitalize()}")
            wrong_answers += 1
    else:
        print("Invalid input! Please enter a number between 1 and 4.")
        wrong_answers += 1
        
    print("--------------------------")
        
print(f"\nYour score is: {score}")
print(f"Total number of correct answers: {correct_answers}")
print(f"Total number of wrong answers: {wrong_answers}")
print("Thank you for playing!")

# Output
# What is the capital of France?
# 1. Berlin
# 2. Rome
# 3. Paris
# 4. London
# Enter your answer (1-4): 3
# Correct!
