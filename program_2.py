# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.

import random
def math_quiz():
    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)

    print(f"   {num1}")
    print(f"+  {num2}")
    print("------")

    user_answer = int(input("Your answer: ")) 
    correct_answer = num1 + num2 
    if user_answer == correct_answer:
        print("Congratulations! You got it right!")
    else:
        print("Sorry, the right answer is {correct_answer}.")
if __name__ == '__main__': 
        print("Welcome to the Simple Math Quiz!")
        math_quiz()
