# Questions and Answers are stored in this 2D arry
import random as rng

def questions(highest_number: int, number_of_questions):
  questions=[]


def generate_question(highest_number: int) -> list:
  # Generate a array containing each whole number from 1 to the highest number chosen
  numbers = range(1, highest_number)
  # Selection of operators in generator math quizzes
  operators = ["+", "-", "*", "/"]
  operator_type = operators[rng.randint(0, 3)]
  # Each question will contain two constants, which are pulled from the Numbers array
  a = numbers[rng.randint(0, highest_number - 1)]
  b = numbers[rng.randint(0, highest_number - 1)]
  # Question is written as a string for when it's returned in the list
  q = f"What is {a} {operator_type} {b}?"]
  # In a array, store the question and, using a eval, calculate the correct answer
  return [q, eval(f"{a} {operator_type} {b}")]