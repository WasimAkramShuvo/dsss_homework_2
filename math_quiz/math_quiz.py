import random

def generate_random_integer(min_value, max_value):
    """
    Generates a random integer within a specified range.
    
    Parameters:
        min_value (int): The minimum value of the range.
        max_value (int): The maximum value of the range.

    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Selects a random arithmetic operator (+, -, or *).
    
    """
    return random.choice(['+', '-', '*'])


def create_problem(num1, num2, operator):
    """
    Creates a math problem based on two numbers and an operator.
    
    Parameters:
        num1 (int): The first operand.
        num2 (int): The second operand.
        operator (str): The operator for the math problem.
        
    """
    problem_statement = f"{num1} {operator} {num2}"
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    return problem_statement, correct_answer


def math_quiz():
    """
    A simple math quiz game that presents the user with math problems and checks their answers.
    """
    score = 0
    total_questions = 3 #here use interger type 

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and operator for the question
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5) #here again use interger type because using random.randint(min_value, myx_value).  
        operator = generate_random_operator()

        problem_statement, correct_answer = create_problem(num1, num2, operator)
        
        # Display the problem and get user's answer
        print(f"\nQuestion: {problem_statement}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue  # Skip to the next question
        
        # Check if the answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    # Display the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
