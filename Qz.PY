# Quiz Game
import random
import time

def quiz():

    # List of questions
    questions = ["What is the capital of France?",
                 "What is the capital of Spain?",
                 "What is the capital of Germany?",
                 "What is the capital of Italy?",
                 "What is the capital of Portugal?",
                 "What is the capital of Greece?",
                 "What is the capital of Poland?",
                 "What is the capital of Ukraine?",
                 "What is the capital of Turkey?",
                 "What is the capital of Russia?"]

    # List of answers
    answers = ["Paris",
               "Madrid",
               "Berlin",
               "Rome",
               "Lisbon",
               "Athens",
               "Warsaw",
               "Kiev",
               "Ankara",
               "Moscow"]

    # List of options
    options = [["Paris", "Madrid", "Berlin", "Rome"],
               ["Madrid", "Paris", "Berlin", "Rome"],
               ["Berlin", "Madrid", "Paris", "Rome"],
               ["Rome", "Madrid", "Berlin", "Paris"],
               ["Lisbon", "Madrid", "Berlin", "Rome"],
               ["Athens", "Madrid", "Berlin", "Rome"],
               ["Warsaw", "Madrid", "Berlin", "Rome"],
               ["Kiev", "Madrid", "Berlin", "Rome"],
               ["Ankara", "Madrid", "Berlin", "Rome"],
               ["Moscow", "Madrid", "Berlin", "Rome"]]
    score = 0
    for i in range(0, 10):
        print(questions[i])
        print("Options:")
        for j in range(0, 4):
            print(str(j+1) + ". " + options[i][j])
        answer = input("Enter your answer: ")
        if answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        print("Score: " + str(score))
        print("\n")
        time.sleep(1)
    print("Your final score is " + str(score) + "/10")

quiz()
